class PaymentMachine:
    # конструктор
    def __init__(self, name, age):
        self.name = name  # имя человека
        self.age = age  # возраст человека
        print("Создание объекта Person")

    def say_hello(self):
        print("Hello" + self.name)
