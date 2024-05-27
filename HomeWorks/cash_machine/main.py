from rich.console import Console
from rich import inspect
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Confirm, IntPrompt
from rich.columns import Columns
from rich.prompt import Confirm, IntPrompt
from rich import box

import os

os.system('color')

console = Console()
list_items = []
amount = []


def add_cas():
    global list_items
    global amount
    items = input('Введите название товара: ')
    price = input('Введите стоимость товара: ')
    print()
    print(''),
    list_items.append(items)
    amount.append(price)


def check_cart(items, price):
    global list_items
    global amount
    items_pnel = Panel(
        Text('\n'.join([f'{item}' for item in items])),
        title="",
        width=34
    )

    amount_panel = Panel(
        Text('\n'.join([f'{amount}' for amount in price])),
        title="",
        width=34
    )

    dub_panel = Columns([items_pnel, amount_panel])
    console.print(dub_panel)


def create_check(items, price):
    total_price = sum([int(i) for i in price])
    len_items = len(items)
    name_saller = 'Королёв Роман'
    street_shop = '''
        Курчатова, 48. Волгодонск
         '''
    console.print(Panel(
        Text(
            f'''
            Большое спасибо за покупку!
                Будем ждать вас ещё!
            ---------------------------
            Кол-во товаров:  {len_items} 
            Общая стоимость: {total_price}р.
            
            Адрес магазина: {street_shop}
            
                    ''',
        ),
        title="Чек",
        width=50
    ))


def clear_cart():
    global list_items
    global amount
    list_items.clear()
    amount.clear()


def run():
    console.print(Panel(Text(
        '''    Выбери одну из операций!
        1. Добавить товар
        2. Что в корзине
        3. Очистить корзину
        4. Создать чек
        5. Завершить работу  
        '''),
        title="Касса.ру",
        width=34
    ))
    while True:
        print()
        oper = console.input("Что хотите сделать? 1-5: ")
        if oper == '1':
            add_cas()
        elif oper == '2':
            check_cart(list_items, amount)
        elif oper == '3':
            clear_cart()
        elif oper == '4':
            create_check(list_items, amount)
        elif oper == '5':
            if Confirm.ask('Вы уверены что хотите выйти?'):
                break
        else:
            print("Введена неверная команда")


run()

