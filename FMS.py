from transitions import Machine


# На этт объект будем вешать состояния
class Matter(object):
    pass


lump = Matter()

# Полный список состояний
states = ['solid', 'liquid', 'gas', 'plasma']

# Добавляем таблицу переходов — из какое в какое состояние мы можем попасть
transitions = [
    {'trigger': 'melt', 'source': 'solid', 'dest': 'liquid'},
    {'trigger': 'evaporate', 'source': 'liquid', 'dest': 'gas'},
    {'trigger': 'sublimate', 'source': 'solid', 'dest': 'gas'},
    {'trigger': 'ionize', 'source': 'gas', 'dest': 'plasma'}
]

# Инициализация машины
machine = Machine(lump, states=states, transitions=transitions, initial='liquid')

# Проверяем начальное состояние
print(lump.state)

# И пробуем изменить состояние триггерами перехода
lump.evaporate()
print(lump.state)
lump.trigger('ionize')
print(lump.state)
