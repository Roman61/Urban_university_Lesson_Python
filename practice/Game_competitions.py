import datetime
import random


class Quest:
    def __init__(self, name, descriptions, lvl, tests):
        self.name = name
        self.descriptions = descriptions
        self.tests = tests
        self.lvl = lvl
        self.status = False
        self.time = None

    def start(self):
        self.time = datetime.datetime.now()

    def check_source(self, source):
        try:
            exec(source, {})
            exec(self.tests, {})
            if eval(self.tests) == eval(source):
                self.time = datetime.datetime.now() - self.time
                self.status = True
                return self.status
            else:
                self.status = False
                return self.status
        except Exception:
            self.status = False
            return self.status


class Person:
    def __init__(self, name, skill, experience, age):
        self.skill = skill
        self.experience = experience
        self.age = age
        self.name = name
        self.__quests = []

    def set_quest(self, quest: Quest):
        self.__quests.append(quest)

    def get_rating(self):
        if self.__quests:
            sum_rating = 0
            for quest in self.__quests:
                if quest.status:
                    sum_rating += quest.lvl / quest.time

            return sum_rating


class Command:
    def __init__(self, name):
        self.name = name
        self.__common_rating = 0
        self.__person_counter = 0
        self.__person = {}

    def add_person(self, person: Person):
        if person:
            self.__person[person.name] = person

    def get_person(self, name):
        return self.__person[name]

    def get_names(self):
        names = []
        for user in self.__person:
            names.append(user.name)
        return names

    def set_quest(self, *quests):
        i = 0
        for quest in quests:
            self.__person[i].set_quest(quest)
            i = self.__randomiser(len(self.__person), len(quests), i)

    @staticmethod
    def __randomiser(person_count: int, quests_count: int, current: int):
        next_index = current + 1
        if next_index >= person_count:
            next_index = 0
        if quests_count > person_count:
            return next_index
        else:
            return random.randint(0, person_count - 1)


class Games:
    def __init__(self):
        self.__commands = []
        self.__quest_common = []

    def add_command(self, command: Command):
        if command:
            self.__commands.append(command)
