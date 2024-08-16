import asyncio
from time import time


async def start_strongman(name, power):
    # name - имя силача
    # power - его подъёмная мощность.
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        await asyncio.sleep(power)
        print(f'Силач {name} поднял {i} шар')
    print(f"Силач {name} закончил соревнования.")


async def start_tournament():
    tasks = []
    strongmen = {'Паша': 3, 'Денис': 4, 'Саша': 5}
    for strongman, power in strongmen.items():
        task = asyncio.create_task(start_strongman(strongman, power))
        tasks.append(task)

    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(start_tournament())

