# Создайте новый класс Buiding
# Создайте инициализатор для класса Buiding, который будет задавать целочисленный атрибут этажности
# self.numberOfFloors и строковый атрибут self.buildingType
# Создайте(перегрузите) __eq__, используйте атрибут numberOfFloors и buildingType для сравнения
# Полученный код напишите в ответ к домашему заданию

class Buiding:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        if self.buildingType == other.buildingType and self.numberOfFloors == other.numberOfFloors:
            return True
        else:
            return False


def main():
    list_buiding = []


    for i in range(2):
        floors = 0
        building_type = ""
        try:
            floors = int(input(f"Введите этажность здания {i + 1}, цифрами: "))
        except TypeError:
            print("Вы ввели не число!")
            return
        if floors < 0:
            print("Число должно быть положительным!")
            return
        building_type = input(f"Напишите тип здания {i + 1}: ")
        if building_type == "":
            print("")
            return
        list_buiding.append(Buiding(floors, building_type))

    if list_buiding[0] == list_buiding[1]:
        print("Здания одинаковые")
    else:
        print("Здания разные")


if __name__ == '__main__':
    main()
