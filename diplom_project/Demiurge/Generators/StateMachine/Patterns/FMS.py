from transitions import Machine, MachineError
from StateMachine.state_map import *
from transitions.extensions import GraphMachine
from transitions import Machine


# На этт объект будем вешать состояния
class Map(object):
    pass


class Maps(object):
    def __init__(self):
        self.lump = Map()
        # Инициализация машины
        self.machine = Machine(self.lump, states=states, transitions=transitions, initial='screen_1_welcome')

    def trigger(self, name):
        try:
            return self.lump.trigger(name)
        except MachineError:
            pass

    def state(self):
        return self.lump.state


if __name__ == "__main__":
    lump = Map()

    # Инициализация машины
    machine = Machine(lump, states=states, transitions=transitions, initial='screen_1_welcome')
    # Проверяем начальное состояние
    print(lump.state)
    print(lump.trigger('btn_help'))
    print(lump.state)

    # И пробуем изменить состояние триггерами перехода
