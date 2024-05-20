import asyncio
from aiogram import Bot, Dispatcher
from aiogram.dispatcher import router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from aiogram import types
from aiogram import F
from aiogram.utils.markdown import hide_link
import os
from rembg import remove
from PIL import Image
from pathlib import Path
from aiogram.types import InputFile

bot = Bot(token='')
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


@dp.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.reply('Привет!' +
                        ' Я умею удалять фон с изображения,' +
                        ' пришли мне картинку и я её обработаю. ')
    print(
        str(message.from_user.id) + " " + message.from_user.username + " " + message.from_user.full_name + ": " + message.text)


@dp.message(F.text == '/help')
async def cmd_start(message: Message):
    await message.reply('Привет!' +
                        ' Я умею удалять фон с изображения,' +
                        ' пришли мне картинку и я её обработаю. ')
    print(
        str(message.from_user.id) + " " + message.from_user.username + " " + message.from_user.full_name + ": " + message.text)


@dp.message(F.photo)
async def download_photo(message: Message, bot: Bot):
    str_ = f'{message.from_user.full_name}, Я принял твою картинку в обработку. Жди'
    await message.answer(str_)
    print(str_)
    filename = f"{message.from_user.full_name}.{message.photo[-1].file_id}.png"
    await bot.download(
        message.photo[-1],
        destination=filename
    )
    await remove_bg(filename)

    filename = f"{message.from_user.full_name}.{message.photo[-1].file_id}_output.png"
    await message.answer_photo(  # _document(#)
        photo=types.FSInputFile(
            path=filename
        ),
        caption=f'{message.from_user.username}, твоё фото обработано!\nМы рады, что Вы пользуетесь нашим ботом!'
    )

    document = FSInputFile(filename)
    await bot.send_document(message.from_user.id, document)

    os.remove(f"{message.from_user.full_name}.{message.photo[-1].file_id}.png")
    os.remove(f"{message.from_user.full_name}.{message.photo[-1].file_id}_output.png")


@dp.message(F.sticker)
async def download_sticker(message: Message, bot: Bot):
    str_ = (f'{message.from_user.full_name}, Я не мею обрабатывать стикеры, извини. Кидай картинки в png, jpg bmp '
            f'форматах')
    await message.answer(str_)


if __name__ == '__main__':
    asyncio.run(main())
