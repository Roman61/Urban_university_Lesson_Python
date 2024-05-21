if __name__ == '__main__':

    a = 10
    b = 20

    print("Helloy I in modul 1")


def summ():
    print(f" result {a + b}")


def sqrt(value):
    return value ** 2


def odd(value):
    if value != 0:
        return value % 2 == 0
    else:
        return None
