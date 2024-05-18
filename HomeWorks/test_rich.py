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

console.print("Привет [b]мир[/b], я [u]твой[/u] отец")
input()
console.clear()
my_list = ['foo', 'bar']
print(inspect(my_list, methods=True))

console.print(":smiley: :vampire: :pile_of_poo: :thumbs_up: :raccoon:")

table = Table(show_header=True, header_style='bold magenta')
table.add_column("Name", style='u', width=12)
console.print(table)
input()
console.clear()
console.print(Panel("Helloy [red]World", title="Welcome", subtitle="Thank"))
input()
console.clear()
list_ = ["[red]Mama[/red]", "Papa", "Baba"]

items_panel = Panel(
    Text.from_markup('\n'.join([f'{item}' for item in list_])),
    title='[blod]Список родителей[/blod]',
    expand=True
)
console.print(items_panel)

age_list = [40, 45, 50]
age_panel = Panel(
    Text('\n'.join([f'{age}' for age in age_list])),
    title='[b]Возраст[/b]',
    expand=True
)

console.print(age_panel)
input()
console.clear()
dub_colums = Columns([items_panel, age_panel])
console.print(dub_colums)

input()
console.clear()

table = Table(title="Todo List")

table.add_column("S. No.", style="cyan", no_wrap=True)
table.add_column("Task", style="magenta")
table.add_column("Status", justify="right", style="green")

table.add_row("1", "Buy Milk", "✅")
table.add_row("2", "Buy Bread", "✅")
table.add_row("3", "Buy Jam", "❌")

console.print(table)