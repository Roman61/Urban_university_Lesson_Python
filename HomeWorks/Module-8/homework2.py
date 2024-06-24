from Active import Agent


class InvalidDataException(Exception):
    def __init__(self, message, info):
        self.message = message
        self.info = info


class ProcessingException(Exception):
    def __init__(self, message):
        self.message = message


class Quest:
    def __init__(self, str_):
        self.ok = False
        if str_ == '':
            raise ProcessingException("Ошибка процесса назначения команд, командная строка пуста!")

        self.key_command_word = ['созда', 'новый', 'проект', 'продолжит', 'функци', 'аргумент', 'генер', 'зависим',
                                 'напишит', 'добав', 'основ', 'вызов', 'обработ', 'проб', 'польз', 'дополн',
                                 'действ', 'внимани', 'ошиб', 'нужн', 'коммент', 'задани', 'наслед', 'пример']

        for i in self.key_command_word:
            if i in str_.lower():
                self.ok = True

        if self.ok:
            self.command_word = str_.split(" ")
        else:
            raise InvalidDataException("Ошибка данных! В задаче не обнаружено ключевых слов", {str_})


def main():
    quests = []
    error_command = False
    while True:
        command_str = input("Введите командную строку или инструкцию к действиям: ")
        if command_str == 'execute':  # исправлние
            break

        while True:
            if command_str == '':
                break
            if not command_str[0:1].isalpha():
                command_str = command_str[1:]
            else:
                break

        try:
            quests.append(Quest(command_str))
        except ProcessingException as pexc:
            print(pexc.message)
            print(pexc.args)
            error_command = True
        except InvalidDataException as idexc:
            print(idexc.message)
            error_command = True

    if len(quests) > 0:
        if error_command:
            print("Внимание часть команд введено не корректно!")

        rabbit = Agent('Rabbit')
        rabbit.run(quests)


if __name__ == "__main__":
    main()




