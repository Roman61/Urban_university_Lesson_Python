import random
from threading import Thread
import asyncio
from faker import Faker


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class Hendlers:
    def __init__(self):
        self.events_hendlers = {}
        self.function = []

    def clear(self):
        self.events_hendlers = {}
        self.function = []

    def hendler(self, event: str, func: callable):
        function = self.events_hendlers.get(event)

        if function is None:
            self.events_hendlers[event] = [func]
        else:
            function.append(func)

    def dispactch(self, event: str, data):
        function = self.events_hendlers.get(event)

        if function is None:
            raise ValueError(f'Unknown event {event}')

        for func in function:
            func(data)


class Fighter:
    def __init__(self, name, strength, armor, health, evasion, accuracy, speed, blocking, weapon, hendler=None):
        self.name: str = name
        self.strength: int = strength  # сила
        self.armor: int = armor  # броня
        self.health: int = health  # здоровье
        self.enemies = []
        self.evasion: int = evasion  # уклонение
        self.accuracy: int = accuracy  # точность
        self.speed: int = speed  # Скорость Атк
        self.blocking: int = blocking  # блокировка
        self.weapon = weapon  # оружие
        self.target = None
        self.event_attack_enemy = None
        self.event_my_is_dead = None
        self.status_attack = False
        if hendler is None:
            self.hendler = Hendlers()
        else:
            self.hendler = hendler

    def event_binding(self):
        self.hendler.hendler('event_attack_enemy', self.event_attack_enemy)
        self.hendler.hendler('event_my_is_dead', self.event_my_is_dead)

    def damage(self):
        pass

    def fight(self, enemy):
        pass

    def attack(self):
        # атака
        self.status_attack = True
        self.hendler.dispactch('event_attack_enemy',
                               {'name': self.name, 'current': self.event_attack_enemy})
        pass

    def protection(self):
        # защита
        self.status_attack = False
        pass

    def actions(self):
        # действия
        if random.randint(1, 20) % 2 == 0:
            self.attack()
        else:
            self.protection()


class Enemy(Fighter):
    def __init__(self, name, strength, armor, health, evasion=1, accuracy=1, speed=5, blocking=1, weapon=1):
        super().__init__(name, strength, armor, health, evasion, accuracy, speed, blocking, weapon)


class Knight(Fighter, Thread):
    def __init__(self, name, strength, evasion=1, accuracy=1, speed=5, blocking=1, weapon=10):
        Thread.__init__(self)
        Fighter.__init__(self, name, strength, armor=10, health=1000, evasion=evasion, accuracy=accuracy, speed=speed,
                         blocking=blocking, weapon=weapon)

    def run(self):
        print(f'{self.name}, на нас напали!"')
        fake = Faker("EN")
        self.enemies = [Enemy(fake.name() + " " + fake.last_name(), fake.random_int(5, 10), fake.random_int(1, 3),
                              fake.random_int(100, 200)) for i in range(100)]
        pass


if __name__ == '__main__':
    # Создание класса
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)
    first_knight.start()
    while True:
        pass
    # Запуск потоков и остановка текущего
    # Вывод строки об окончании сражения
