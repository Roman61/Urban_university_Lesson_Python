# from tqdm import tqdm
# from tqdm.notebook import tqdm_notebook
# import time
#
# print('test', end='\r')
# print('abcd', end='\r')
#
# for i in tqdm(range(20), desc='tqdm() Progress Bar'):
#     time.sleep(0.1)
#
# for i in tqdm(range(2), desc='Loop 1'):
#     for j in tqdm(range(20, 25), desc='Loop 2'):
#         time.sleep(0.1)


# from tqdm import tqdm
# import time
#
# # Define the total number of iterations for the progress bar
# total_iterations = 100
#
# # Create a tqdm progress bar
# progress_bar = tqdm(total=total_iterations, desc="Processing")
#
# # Simulate some task that iterates
# for i in range(total_iterations):
#     # Do some processing here
#     time.sleep(0.1)  # Simulating a delay
#
#     # Update the progress bar
#     progress_bar.update(1)
#
# # Close the progress bar
# progress_bar.close()
#
# print("Task completed!")
from rich.console import Console
from rich.table import Table
from rich.console import Console

table = Table(title="Star Wars Movies")

table.add_column("Released", justify="right", style="cyan", no_wrap=True)
table.add_column("Title", style="magenta")
table.add_column("Box Office", justify="right", style="green")

table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")

console = Console()
console.print(table)
