from crud_functions import Engine

# with Engine("database.db") as engine:
#     engine.drop_table_products()
#     engine.initiate_db()
#     for i in engine.get_all_products():
#         print(i)

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
button_buy_inl = InlineKeyboardButton(text='Купить', callback_data='buy')
button_m_inl = InlineKeyboardButton(text='мужской', callback_data='male')
button_w_inl = InlineKeyboardButton(text='женский', callback_data='female')
button_buy_1 = InlineKeyboardButton(text='Продукт 1', callback_data="product_1"
                                    # ,url='https://shop.pro-zdorovie.ru/biodobavki/gel-bolotova/gel-bolotova-zdorovye-sustavy-tm-tsentr-bolotova/'
                                    )
button_buy_2 = InlineKeyboardButton(text='Продукт 2', callback_data="product_2"
                                    #, url='https://shop.pro-zdorovie.ru/biodobavki/gel-bolotova/gel-bolotova-ot-varikoza/'
                                    )
button_buy_3 = InlineKeyboardButton(text='Продукт 3', callback_data="product_3"
                                    # , url='https://shop.pro-zdorovie.ru/biodobavki/kontsentrat-serebra-aqua-vitae/'
                                    )
button_buy_4 = InlineKeyboardButton(text='Продукт 4', callback_data="product_4",
                                    # url='https://shop.pro-zdorovie.ru/biodobavki/orzax-milk-thistle-plus/'
                                    )
back_to_cat = InlineKeyboardButton(text="Назад", callback_data="back_to_catalog")

kbi = InlineKeyboardMarkup(inline_keyboard=[[button_calories_inl, button_formulas_inl], [button_buy_inl], ])
kbi_sex = InlineKeyboardMarkup(inline_keyboard=[[button_m_inl, button_w_inl], ])
buy_kb = InlineKeyboardMarkup(inline_keyboard=[[button_buy_1, button_buy_2, button_buy_3, button_buy_4], [back_to_cat]])

calc_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Рассчитать")],
    ],
    resize_keyboard=True
)

# dietary_supplements = {
#     'Здоровые суставы': ['files/1.jpg', '1400 ₽', 'Гель Болотова "Здоровые суставы", ТМ "Центр Болотова" 100 мл.'],
#     'От варикоза': ['files/2.jpg', '1400 ₽', 'Гель Болотова от варикоза, ТМ "Центр Болотова"'],
#     'AQUA VITAE': ['files/3.jpg', '1100 ₽', 'Концентрат Серебра AQUA VITAE'],
#     'Orzax Milk': ['files/4.jpg', '2100 ₽', 'ОРЗАКС МОЛОЧНЫЙ РАСПОРОПШИ ПЛЮС'],
# }


class UserState(StatesGroup):
    sex = State()
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=["start"])
async def start(message):
    with Engine("database.db") as engine:
        engine.drop_table_products()
        engine.initiate_db()
    await message.answer(f"Привет {message['from']['first_name']}! Могу расчитать необходимые тебе колоррии для "
                         f"похудения или сохранения"
                         f" нормального веса. Введи команду Рассчитать и следуй инструкциям!", reply_markup=calc_kb)


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


@dp.callback_query_handler(text="")
async def mega_t(call):
    await call.message.answer('Вы успешно приобрели продукт!', reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text="buy")
async def get_buying_list(call):
    with Engine("database.db") as engine:
        engine.drop_table_products()
        engine.initiate_db()
        for i in engine.get_all_products():
            print(i)
            with open(i[4], "rb") as img:
                await call.message.answer_photo(img, f'Название: {i[1]} | Описание: {i[2]} | Цена: {i[3]}>')
    await call.message.answer("Выберете продукт для покупки:", reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text="back_to_catalog")
async def back(call):
    await call.message.answer("Выберите опцию:", reply_markup=kbi)
    await call.answer()


@dp.callback_query_handler(text="product_1")
async def back(call):
    await call.message.answer("Вы успешно приобрели товар!")
    await call.answer()


@dp.callback_query_handler(text="product_2")
async def back(call):
    await call.message.answer("Вы успешно приобрели товар!")
    await call.answer()


@dp.callback_query_handler(text="product_3")
async def back(call):
    await call.message.answer("Вы успешно приобрели товар!")
    await call.answer()


@dp.callback_query_handler(text="product_4")
async def back(call):
    await call.message.answer("Вы успешно приобрели товар!")
    await call.answer()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
