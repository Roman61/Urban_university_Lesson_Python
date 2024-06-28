class OperationError(Exception):
    def __init__(self, message, info):
        self.message = message
        self.info = info


class Executor:
    def __init__(self):
        self.lambda_method = False
        self.separators = ['+', '-', '*', '/', '%', '//', '**', '&', '|', '^', '~', '<<', '>>']

    def __default_sep(self, prisoner, separator, print_=False):
        try:
            x, autodafe, y = prisoner.split(separator)
            execute = self.execute_fabric(autodafe)
            if print_:
                print(f'Входные данные ({x} {autodafe} {y}) ', end='')
            x, y = int(x), int(y)
            return execute(x, y)
        except ValueError:
            self.__another_sep(prisoner)

    def __another_sep(self, prisoner, print_=False):
        autodafe = ''
        execute = None
        for sep in self.separators:
            if sep in prisoner:
                autodafe = sep
                break
        if autodafe != '':
            x, y = prisoner.split(autodafe)
            if print_:
                print(f'Входные данные ({x} {autodafe} {y})', end='')
            if self.lambda_method:
                execute = self.execute_lambda_fabric(autodafe)
            else:
                execute = self.execute_fabric(autodafe)
            x, y = int(x), int(y)
            result_ = int(execute(x, y))
            return result_
        else:
            raise OperationError(
                "Хой, гуманитарий, давай полегче, я просил математическое выражение, а не стихотворение Пушкина.",
                prisoner)

    def __call__(self, prisoner, separator=' ', lambda_=False, print_=False):
        self.lambda_method = lambda_
        out_ = None
        str_ = ''
        if lambda_:
            str_ = 'лямбда метод вернул значение'
        else:
            str_ = 'фабрика функций вернула значение'
        if separator in prisoner:
            out_ = self.__default_sep(prisoner, separator, print_)
        else:
            out_ = self.__another_sep(prisoner, print_)
        if print_:
            print(f'{str_}: {out_}')
        return out_

    def execute_fabric(self, types):
        if types == '+' or types == 'add':
            def addition(x, y):
                return x + y  # сложение

            return addition
        elif types == '-' or types == 'sub':
            def subtraction(x, y):
                return x - y  # вычитание

            return subtraction
        elif types == '*' or types == 'mult':
            def multiplication(x, y):
                return x * y  # умножение

            return multiplication
        elif types == '/' or types == 'div':
            def division(x, y):
                return x / y  # деление

            return division
        elif types == '%' or types == 'rem':
            def remainder_of_the_division(x, y):
                return x % y  # остаток от деления

            return remainder_of_the_division
        elif types == '//' or types == 'comp':
            def complete_division(x, y):
                return x // y  # деление нацело

            return complete_division
        elif types == '**' or types == 'exp':
            def exponentiation(x, y):
                return x ** y  # возведение в степень

            return exponentiation
        elif types == '&' or types == 'and':
            def and_(x, y):
                return x & y  # И

            return and_
        elif types == '|' or types == 'or':
            def or_(x, y):
                return x | y  # ИЛИ

            return or_
        elif types == '^' or types == 'not':
            def not_(x, y):
                return x ^ y  # XOR

            return not_
        elif types == '~' or types == 'xor':
            def xor_(x, y):
                return ~x | ~y  # НЕ

            return xor_
        elif types == '<<' or types == 'left':
            def shift_right(x, y):
                return x << y  # сдвиг влево

            return shift_right
        elif types == '>>' or types == 'right':
            def shift_left(x, y):
                return x >> y  # сдвиг вправо

            return shift_left

    def execute_lambda_fabric(self, types):
        if types == '+' or types == 'add':
            return lambda x, y: x + y  # сложение
        elif types == '-' or types == 'sub':
            return lambda x, y: x - y  # вычитание
        elif types == '*' or types == 'mult':
            return lambda x, y: x * y  # умножение
        elif types == '/' or types == 'div':
            return lambda x, y: x / y  # деление
        elif types == '%' or types == 'rem':
            return lambda x, y: x % y  # остаток от деления
        elif types == '//' or types == 'comp':
            return lambda x, y: x // y  # деление нацело
        elif types == '**' or types == 'exp':
            return lambda x, y: x ** y  # возведение в степень
        elif types == '&' or types == 'and':
            return lambda x, y: x & y  # И
        elif types == '|' or types == 'or':
            return lambda x, y: x | y  # ИЛИ
        elif types == '^' or types == 'not':
            return lambda x, y: x ^ y  # XOR
        elif types == '~' or types == 'xor':
            return lambda x, y: ~x | ~y  # НЕ
        elif types == '<<' or types == 'left':
            return lambda x, y: x << y  # сдвиг влево
        elif types == '>>' or types == 'right':
            return lambda x, y: x >> y  # сдвиг вправо


class Rect:
    def __init__(self, a, b, print_=False):
        self.a = a
        self.b = b
        self.print_ = print_
        if self.print_:
            print(f'Стороны: {self.a}, {self.b}')

    def __call__(self):
        executor = Executor()
        res = executor(str(self.a) + "*" + str(self.a))
        if self.print_:
            print(f'Площадь: {res}')
        return res


if __name__ == '__main__':
    executor = Executor()
    print("Задача 1:")
    executor("5 + 5", print_=True)
    executor("7 * 8", print_=True)
    executor("5 / 5", print_=True)
    print("Задача 2:")
    executor("5 + 5", lambda_=True, print_=True)
    executor("7 * 8", lambda_=True, print_=True)
    executor("5 / 5", lambda_=True, print_=True)
    print("Задача 3: Вызываемые объекты")
    rect = Rect(5, 5, print_=True)
    rect()
