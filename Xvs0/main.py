# from game import draw
import game
from game import arena, victory, step, step_char

print("Добро пожаловать в игру 'Крестики Нолики'!")
print("Правила:")
print("В игре учавствуют 2 игрока, игра происодит на поле с нечётным количеством клеток.")

while not arena:
    is_default = ""
    while not (is_default == "Y" or is_default == "y" or is_default == "N" or is_default == "n"):
        is_default = input("Выбрать размер поля по умолчанию 3х3? y/n  ")

    if is_default == "y" or is_default == "Y":
        arena = game.init()
    else:
        width = int(input("Введите ширину поля: "))
        height = int(input("Введите ширину поля: "))

        arena = game.init(width, height)

    if not arena:
        print("Нарушение правила!")
        print("Размер поля должен быть нечетным по высоте и ширине.")
        exit_ = ""
        while not (exit_ == "Y" or exit_ == "y" or exit_ == "N" or exit_ == "n"):
            exit_ = input("Желаете начать с начала? y/n  ")
        if exit_ == "n" or exit_ == "N":
            print("Выход из игры!")
            exit    ()

while not victory:
    game.draw(arena)
    step += 1
    print(f'Ход {step}!')
    if step % 2 == 1:
        print("Теперь ходят крестики!")
        step_char = 'X'
    else:
        print("Теперь ходят нолики!")
        step_char = 'O'
    row = int(input(f'Введите номер строки от 1 до {len(arena)}: ')) - 1
    column = int(input(f'Введите номер столбца от 1 до {len(arena[0])}: ')) - 1
    arena[row][column] = step_char

    n = 3
    for i in range(0, n):
        for j in range(0, n):
            if i == 0 or i == n - 1 or j == i or j == n - i - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
