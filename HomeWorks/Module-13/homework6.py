from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import asyncio
from config import api

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

button_calories_inl = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_formulas_inl = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
button_m_inl = InlineKeyboardButton(text='мужской', callback_data='male')
button_w_inl = InlineKeyboardButton(text='женский', callback_data='female')

kbi = InlineKeyboardMarkup(inline_keyboard=[[button_calories_inl, button_formulas_inl], ])
kbi_sex = InlineKeyboardMarkup(inline_keyboard=[[button_m_inl, button_w_inl], ])


class UserState(StatesGroup):
    sex = State()
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer(f"Привет {message['from']['first_name']}! Могу расчитать необходимые тебе колоррии для "
                         f"похудения или сохранения"
                         f" нормального веса. Введи команду Рассчитать и следуй инструкциям!")


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup=kbi)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer("для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;  "
                              "для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161")
    await call.answer()


@dp.callback_query_handler(text="calories")
async def set_sex(call):
    await call.message.answer("Введи свой пол(м/ж): ", reply_markup=kbi_sex)
    await call.answer()


@dp.callback_query_handler(text="male")
async def set_age(call):
    await UserState.sex.set()
    state = Dispatcher.get_current().current_state()
    await state.update_data(sex="м")
    await call.message.answer(f"Введи свой возраст(г):")
    await call.answer()
    await UserState.age.set()


@dp.callback_query_handler(text="female")
async def set_age(call):
    await UserState.sex.set()
    state = Dispatcher.get_current().current_state()
    await state.update_data(sex="ж")
    await call.message.answer(f"Введи свой возраст(г):")
    await call.answer()
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=int(message.text))
    await message.answer(f"Введи свой рост(см):")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=int(message.text))
    await message.answer(f"Введи свой вес(кг):")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    calories = 0
    try:
        if str(data['sex']).lower() == "м":
            calories = (10 * data["weight"]) + (6.25 * data["growth"]) - (5 * data["age"]) + 5
        elif str(data['sex']).lower() == "ж":
            calories = (10 * data["weight"]) + (6.25 * data["growth"]) - (5 * data["age"]) + 161
    except:
        await message.answer(f"упс! Ты сломал интернет!")
    if calories == 0:
        await message.answer(f"Введены некорректные данные.")
    else:
        await message.answer(f"Твоя норма: {calories} ккал в сутки!")
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
