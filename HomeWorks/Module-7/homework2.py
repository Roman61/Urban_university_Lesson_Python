# Ваша задача:
# Создайте в директории проекта текстовый файл с расширением txt
# Добавьте в этот файл следующий текст
#
# Создайте переменную с этим файлом
# Распечатайте содержимое текстового файла в консоль, используя оператор with
# Чем отличается использование оператора with open(file_name...) от простого использования file.close()?
# Получившийся код прикрепите к заданию текстом
# Создайте переменную с этим файлом
# Распечатайте содержимое текстового файла в консоль
# Закройте файл
file_name = ' Byron.txt'
with open(file_name, mode='r') as file:
    file_content = file.read()
print(file_content)

