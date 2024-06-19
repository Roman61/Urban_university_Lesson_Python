import os
import time

# os.walk, os.path.join, os.path.getmtime, os.path.dirname, os.path.getsize

directory = "."
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root + '/' + file)
        filetime = os.path.getmtime(root + '/' + file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(root + '/' + file)
        parent_dir = root
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, '
            f'Родительская директория: {parent_dir}')
