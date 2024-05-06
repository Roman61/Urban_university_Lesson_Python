import asyncio
from aiogram import Bot, Dispatcher
from aiogram.dispatcher import router
from aiogram.filters import Command
from aiogram.types import Message, InputFile, FSInputFile
from aiogram import types
from aiogram import F
from aiogram.utils.markdown import hide_link
import os
from rembg import remove
from PIL import Image
from pathlib import Path

bot = Bot(token='7026873368:AAF-dT6eJ31l1aQhAJyLGNnIkQ1qI6g7tWc')
dp = Dispatcher()


async def main():
    await dp.start_polling(bot)


async def remove_bg(filename):
    list_of_extension = ['*.png', '*.jpg']
    all_files = [filename]

    # for ext in list_of_extension:Path('input_imgs').glob(ext)

    print(all_files)

    for index, item in enumerate(all_files):
        input_path = Path(item)
        file_name = input_path.stem

        output_path = f'{file_name}_output.png'
        input_img = Image.open(input_path)

        # Downloading data from 'https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net.onnx'
        # to file 'C:\Users\Admin\.u2net\u2net.onnx'.
        output_img = remove(input_img)
        output_img.save(output_path)

        print(f'Completed: {index + 1}/{len(all_files)}')


@dp.message(F.text)
async def cmd_start(message: Message):
    await message.reply('Привет!' +
                        ' Это тестовый запуск, если ты напишешь сообщеиние я его увижу! ' +
                        'Можешь писать пожелания и идеи для бота сюда. ' + message.text)
    print(
        str(message.from_user.id) + " " + message.from_user.username + " " + message.from_user.full_name + ": " + message.text)


@dp.message(F.photo)
async def download_photo(message: Message, bot: Bot):
    filename = f"{message.from_user.full_name}.{message.photo[-1].file_id}.png"
    await bot.download(
        message.photo[-1],
        destination=filename
    )
    await remove_bg(filename)

    str_ = (str(message.from_user.id) + " " + message.from_user.full_name + ": Прислал картинку " + filename)
    await message.answer(str_)
    print(str_)

    filename = f"{message.from_user.full_name}.{message.photo[-1].file_id}_output.png"
    await message.answer_photo(#_document(#)
        photo=types.FSInputFile(
            path=filename
        ),
        caption=f'{message.from_user.full_name}, твоё фото обработано!\nМы рады что вы пользуйтесь нашим ботом!'
    )

    # document = FSInputFile(path=filename)
    # await message.send_document(Message.chat.id, document)

    os.remove(f"{message.from_user.full_name}.{message.photo[-1].file_id}.png")
    # os.remove(f"{message.from_user.full_name}.{message.photo[-1].file_id}_output.png")


@dp.message(F.sticker)
async def download_sticker(message: Message, bot: Bot):
    await bot.download(
        message.sticker,
        # для Windows пути надо подправить
        destination=f"/tmp/{message.sticker.file_id}.webp"
    )


if __name__ == '__main__':
    asyncio.run(main())
