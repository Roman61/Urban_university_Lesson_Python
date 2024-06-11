import hashlib


class User:
    def __init__(self, nickname, password, age):
        self.nickname: str = nickname
        self.password: str = self.__password_hash(password)  # в хэшированном виде
        self.age: int = age

    def password_verify(self, password):
        return self.__password_hash(password) == self.password

    def __password_hash(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def __str__(self):
        return self.nickname

    def __repr__(self):
        return self.nickname