import math


class Figure:
    def __init__(self, *args):
        if self.sides_count == None:
            self.sides_count: int = 0
        self.__sides = []
        self.__color = []
        self.filled: bool = False
        sides_args = args[1::]
        color_args = args[0:1:]
        self.set_sides(*sides_args)
        self.set_color(*color_args[0])

    def get_sides(self):
        return self.__sides

    def set_sides(self, *args):
        assert self.__is_valid_sides(*args)
        self.__sides = []
        if len(args) > 1:
            self.__sides = list(args)
        else:
            for i in range(0, self.sides_count):
                j = args[0]
                self.__sides.append(j)
        self.__event_add_sides(*self.__sides)

    def __event_add_sides(self, *args):
        pass

    def __is_valid_sides(self, *args):
        if len(args) == self.sides_count or len(args) == 1:
            return True
        else:
            return False

    def __len__(self):
        if self.__sides:
            return sum(self.__sides)
        else:
            return 0

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if self.__check_color(r) and self.__check_color(g) and self.__check_color(b):
            return True
        else:
            return False

    @staticmethod
    def __check_color(color_chanel):
        if 0 <= color_chanel <= 255:
            return True
        else:
            return False


class Circle(Figure):
    def __init__(self, *args):
        self.sides_count = 1
        self.__radius = 0  # , рассчитать исходя из длины окружности (одной единственной стороны).
        super().__init__(*args)

    def __event_add_sides(self, *args):
        self.__radius = args[0] / (math.pi * 2)

    def get_square(self):
        """возвращает площадь круга (можно рассчитать как через длину, так и через радиус)."""
        if self.__radius:
            return math.pi * (self.__radius * self.__radius)


class Triangle(Figure):
    def __init__(self, *args):
        self.sides_count = 3
        super().__init__(*args)

    def get_square(self):
        # возвращает площадь треугольника.
        p = len(self) / 2
        a = self.get_sides()[0]
        b = self.get_sides()[1]
        c = self.get_sides()[2]
        return math.sqrt(p) * (p - a)*(p - b)*(p - c)


class Cube(Figure):
    def __init__(self, *args):
        self.sides_count = 12
        super().__init__(*args)

    def get_volume(self):  # возвращает объём куба
        return self.get_sides()[0] ** 3


if __name__ == '__main__':
    # При создании объектов делайте проверку на количество переданных сторон, если сторон не ровно sides_count, то
    # создать массив с единичными сторонами и в том кол-ве, которое требует фигура.
    # Circle((200, 200, 100), 10, 15, 6)  # , т.к. сторона у круга всего 1, то его стороны будут - [1]
    # Triangle((200, 200, 100), 10, 6)  # , т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]
    # Cube((200, 200, 100), 9)  # , т.к. сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)
    # Cube((200, 200, 100), 9, 12)  # , т.к. сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    cube1.set_color(300, 70, 15)  # Не изменится
    print(circle1.get_color())
    print(cube1.get_color())

    # Проверка на изменение сторон:
    # cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    circle1.set_sides(15)  # Изменится
    print(cube1.get_sides())
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())

