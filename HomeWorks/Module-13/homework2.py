from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from config import api

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(text=["1"])
async def test_massage(message):
    print(" Мы получили тестовое сообщение! ", message["text"])


@dp.message_handler(commands=["start"])
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
async def all_massage(message):
    print("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)