# Создайте новый класс Buiding с атрибутом total
# Создайте инициализатор для класса Buiding, который будет увеличивать атрибут количества созданных
# объектов класса Building total (по примеру класса Lemming из урока)
# В цикле создайте 40 объектов класса Building и выведите их на экран командой print
# Полученный код напишите в ответ к домашнему заданию
total = 0


class Buiding:
    def __init__(self):
        global total
        total += 1
        print(f'Объектов создано {total}')


def main():
    list_buiding = []

    for i in range(40):
        list_buiding.append(Buiding())


if __name__ == '__main__':
    main()
