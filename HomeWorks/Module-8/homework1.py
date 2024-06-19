def add_everything_up(a, b):
    try:
        return f'{(a + b):0.3f}'
    except TypeError:
        return str(a) + str(b)
    except ValueError:
        return str(a) + str(b)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

