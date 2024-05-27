# Создайте новый класс House
# Создайте инициализатор для класса House,
# который будет задавать атрибут этажности self.numberOfFloors = 0
# Создайте метод setNewNumberOfFloors(floors),
# который будет изменять атрибут numberOfFloors на параметр floors и
# выводить в консоль numberOfFloors

class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(f'Этажей в здании: {self.numberOfFloors}')


def main():
    house = House()
    try:
        floors = int(input("Введите этажность здания цифрами: "))
        house.setNewNumberOfFloors(floors)
    except TypeError:
        print("Вы ввели не число!")


if __name__ == '__main__':
    main()
