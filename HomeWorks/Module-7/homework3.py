# Пример входных данных
commands = [
    {'name': "Мастера кода", 'num': 6, 'score': 40, 'time': 1552.512},
    {'name': "Волшебники данных", 'num': 6, 'score': 42, 'time': 2153.31451}
]

users = 0
tasks_total = 0
time_total = 0
challenge_result = "Ничья!"

for cmd in commands:
    print('В команде "%s" участников: %d!' % (cmd['name'], cmd['num']))
    users += cmd['num']

print("Итого сегодня %d участников!" % users)

for cmd in commands:
    print('Команда "{}" решила задач: {}!'.format(cmd['name'], cmd['score']))

for cmd in commands:
    print('Команда "{0}" решили задачи за {1:.2f} с!'.format(cmd['name'], cmd['time']))

for cmd in commands:
    tasks_total += cmd['score']
    time_total += cmd['time']
time_avg = time_total / tasks_total

for j in range(0, len(commands)):
    for i in range(0, len(commands)):
        if commands[j]['name'] != commands[i]['name']:
            if commands[j]['score'] > commands[i]['score'] or commands[j]['score'] == commands[i]['score'] and \
                    commands[j]['time'] > commands[i]['score']:
                challenge_result = commands[j]['name']
            elif commands[j]['score'] < commands[i]['score'] or commands[j]['score'] == commands[i]['score'] and \
                    commands[j]['time'] < commands[i]['score']:
                challenge_result = commands[i]['name']

print(f'Результат битвы: победа команды "{challenge_result}"!')
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.2f} секунды на задачу!")
