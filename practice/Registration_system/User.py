import random
from re import search
from faker import Faker


class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, in_user):
        self.data[in_user.username] = in_user.password


class User:
    """
        Класс пользователя, содержащий атрибуты: Логин, пароль.
    """

    def __init__(self):
        self.ok = False
        self.password = ''
        self.username = 'Гость'
        self.validation_length = False
        self.length_min = 8
        self.validation_digital = False
        self.validation_upper_case = False

    def get_doc(self):
        return self.__doc__

    def create(self, username, password, password_confirm):
        self.ok = False
        self.username = 'Гость'
        if self.validation_length and not len(password) > self.length_min:
            print(f"{len(password)}<{self.length_min}")
            return
        if self.validation_upper_case and not search(r'[A-Z]', password):
            print(f"empty [A-Z]")
            return
        if self.validation_digital and not search(r'[0-9]', password):
            print(f"empty [0-9]")
            return
        if password_confirm != password:
            print(f"{password_confirm} не равно {password}")
            return
        self.password = password
        self.username = username
        self.ok = True


if __name__ == '__main__':
    database = Database()
    user = User()
    user.validation_digital = True
    user.validation_upper_case = True
    user.validation_length = True
    while True:
        choice = input(f'Приветствую, {user.username}! Выбери действие: \n1 - Вход\n2 - Регистрация\n')
        if choice == '1':
            login = input('')
            password = input('')
            if login in database.data:
                if password == database.data[login]:
                    print(f'Helloy {login}')
                    break
                else:
                    print('password uncorrected')
                print('ok')
            else:
                print('not find user')
        if choice == '2':
            user.create(input("Введите логин: "), input("Введите пароль: "), input("Подтвердите пароль: "))
            if user.ok:
                database.add_user(user)
                print(database.data)
            else:
                print("Не корректный ввод!")
