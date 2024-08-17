from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from config import api

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(text=["1"])
async def test_massage(message):
    print(" Мы получили тестовое сообщение! " + message["text"])
    await message.answer(" Мы получили тестовое сообщение! "+ message.text)


@dp.message_handler(commands=["start"])
async def start(message):
    text = 'Привет! Я бот помогающий твоему здоровью.'
    print(text)
    await message.answer(text)


@dp.message_handler()
async def all_massage(message):
    text = "Введите команду /start, чтобы начать общение."
    print(text)
    await message.answer(text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
