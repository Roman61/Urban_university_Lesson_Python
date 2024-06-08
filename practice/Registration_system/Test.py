import random

from faker import Faker

from practice.Registration_system.User import Database, User


def test_user_add_validation_full():
    fake = Faker("ru_RU")
    fake_password = Faker("en_US")

    database_t_add = Database()
    user_t_add = User()
    user_t_add.validation_digital = True
    user_t_add.validation_upper_case = True
    user_t_add.validation_length = True

    for i in range(0, random.randint(1, 50)):
        username = fake.name()
        password = fake_password.password()
        password_confirm = password
        user_t_add.create(username, password, password_confirm)
        database_t_add.add_user(user_t_add)
        assert database_t_add.data[username] == password
    pass


def test_user_add():
    fake = Faker("ru_RU")
    fake_password = Faker("en_US")

    database_t_add = Database()
    user_t_add = User()
    user_t_add.validation_digital = False
    user_t_add.validation_upper_case = False
    user_t_add.validation_length = False

    for i in range(0, random.randint(1, 50)):
        username = fake.name()
        password = fake_password.password()
        password_confirm = password
        user_t_add.create(username, password, password_confirm)
        database_t_add.add_user(user_t_add)
        assert database_t_add.data[username] == password
    pass


def test_user_add_validation_length():
    fake = Faker("ru_RU")
    fake_password = Faker("en_US")

    database_t_add = Database()
    user_t_add = User()
    user_t_add.validation_digital = False
    user_t_add.validation_upper_case = False
    user_t_add.validation_length = True

    for i in range(0, random.randint(1, 50)):
        username = fake.name()
        password = fake_password.password()
        password_confirm = password
        user_t_add.create(username, password, password_confirm)
        database_t_add.add_user(user_t_add)
        assert database_t_add.data[username] == password
    pass


def test_user_add_validation_upper_case():
    fake = Faker("ru_RU")
    fake_password = Faker("en_US")

    database_t_add = Database()
    user_t_add = User()
    user_t_add.validation_digital = False
    user_t_add.validation_upper_case = True
    user_t_add.validation_length = False

    for i in range(0, random.randint(10, 50)):
        username = fake.name()
        password = fake_password.password()
        password_confirm = password
        user_t_add.create(username, password, password_confirm)
        database_t_add.add_user(user_t_add)
        assert database_t_add.data[username] == password
    pass


def test_user_add_validation_digital():
    fake = Faker("ru_RU")
    fake_password = Faker("en_US")

    database_t_add = Database()
    user_t_add = User()
    user_t_add.validation_digital = True
    user_t_add.validation_upper_case = False
    user_t_add.validation_length = False

    for i in range(0, random.randint(1, 50)):
        username = fake.name()
        password = fake_password.password()
        password_confirm = password
        user_t_add.create(username, password, password_confirm)
        database_t_add.add_user(user_t_add)
        assert database_t_add.data[username] == password
    pass
