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
kb = ReplyKeyboardMarkup()
button = KeyboardButton(text="Информация")
button2 = KeyboardButton(text="Начало")
# kb.add(button)
# kb.add(button2)

kbi = InlineKeyboardMarkup()
button_1_inf_inl = InlineKeyboardButton(text="Информация", callback_data='info')
# button_2_inf_inl = InlineKeyboardButton(text="Помощь", callback_data='help')
kbi.add(button_1_inf_inl)


# kbi.add(button_2_inf_inl)


# kb.row() kb.insert()

class UserState(StatesGroup):
    address = State()


start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='info')],
        [
            KeyboardButton(text="shop"),
            KeyboardButton(text="donate")
        ]
    ],
    resize_keyboard=True
)


@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer("Привет!", reply_markup=start_menu)


@dp.callback_query_handler(text='info')
async def infor(call):
    await call.message.answer("Информация о боте")
    await call.answer()


@dp.message_handler(text="Информация")
async def inform(message):
    await message.answer("Информация о боте")


@dp.message_handler(text="Заказать")
async def buy(message):
    await message.answer("Отправь нам свой адрес, пожалуйста.")
    await UserState.address.set()


@dp.message_handler(state=UserState.address)
async def fms_handler(message, state):
    await state.update_data(first=message.text)
    data = await state.get_data()
    await message.answer(f"Доставка будет отправлена на {data['first']}")
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
