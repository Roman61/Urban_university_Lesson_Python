from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import asyncio
from config import api

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

button1 = KeyboardButton(text="Информация")
button2 = KeyboardButton(text="Рассчитать")

button_men = KeyboardButton(text="м")
button_women = KeyboardButton(text="ж")

kb_sex = ReplyKeyboardMarkup(keyboard=[[button_men, button_women], ], resize_keyboard=True)
kb = ReplyKeyboardMarkup(keyboard=[[button1, button2], ], resize_keyboard=True)


# kb.add()
# kb.add()


class UserState(StatesGroup):
    sex = State()
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer("Привет!", reply_markup=kb)


@dp.message_handler(text="Рассчитать")
async def buy(message):
    await message.answer(f"Привет {message['from']['first_name']}! Сейчас мы расчитаем необходимые колоррии для "
                         f"похудения или сохранения"
                         f" нормального веса. Следуй инструкциям!")
    await message.answer("Введи свой пол(м/ж): ", reply_markup=kb_sex)
    await UserState.sex.set()


@dp.message_handler(state=UserState.sex)
async def set_age(message, state):
    await state.update_data(sex=message.text)
    await message.answer(f"Введи свой возраст(г):")
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
