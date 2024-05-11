from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Confirm, IntPrompt
from rich.columns import Columns


def func():
    n = int(input("Введите число: "))
    for i in range(1, n + 1):
        # list_x[:] = [f(tup) for tup in zip(list_x, list_y)]
        f = lambda: int(input("Введите числа: ").split(' '))
        num = [f for j in range(1, x)]
        print(num)


func()
