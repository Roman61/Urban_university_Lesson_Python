import hashlib
import pytest
from User import User
from faker import Faker

fake = Faker()


def test_init():
    nickname = fake.user_name()
    password = fake.password()
    age = fake.pyint(min_value=18, max_value=80)
    user = User(nickname, password, age)
    assert user.nickname == nickname
    assert user.age == age
    assert user.password_verify(password)


def test_password_verify():
    nickname = fake.user_name()
    password = fake.password()
    age = fake.pyint(min_value=18, max_value=80)
    user = User(nickname, password, age)
    assert user.password_verify(password)
    assert not user.password_verify("wrongpassword")


def test_password_hash():
    nickname = fake.user_name()
    password = fake.password()
    age = fake.pyint(min_value=18, max_value=80)
    user = User(nickname, password, age)
    assert len(user.password) == 64
    assert user.password == hashlib.sha256(password.encode()).hexdigest()



