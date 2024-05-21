from nim_ingine import get_bunches, take_frome_bunch, is_gameover, put_stones
from termcolor import cprint
from termcolor import colored
put_stones()
user_number = 1
while True:
    cprint('Текущая позиция: ', color='green')
    user_color = 'blue' if user_number == 1 else 'yellow'
    cprint(get_bunches(), color='green')
    cprint(f'Ходит ирок - {user_number}.', color=user_color)
    pos = 0
    qua = 0
    try:
        pos = int(colored(input('Откуда берём? '), color=user_color))
        qua = int(colored(input('Сколько берём? '), color=user_color))
    except ValueError:
        cprint(f'Игрок - {user_number} пропскает ход!')
        user_number = 2 if user_number == 1 else 1
        continue
    if pos <= 0 or qua <= 0:
        cprint(f'Игрок - {user_number} прервал раунд')
        exit()
    take_frome_bunch(position=int(pos), quantity=int(qua))
    if is_gameover():

        break

    user_number = 2 if user_number == 1 else 1

cprint(f'Выиграл игрок {user_number}', color='red')
