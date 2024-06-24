class Agent:
    def __init__(self, name):
        self. name = name
        print(f"Здраствуйте, я ваш личный ассистент, меня зовут {self. name}")
        print("Готов исполнить ваши задания")
        self._quest_array = None

    def run(self, quest_array):
        print(f"{len(quest_array)} заданий приняты к исполнению.")
        self._quest_array = quest_array
