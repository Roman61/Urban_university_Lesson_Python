def print_params(a=1, b='строка', c=True):
    print(a, b, c)


list_ = [2, 'текст', False]

print_params()
print_params(*list_)
print_params(list_,2,3)
print_params(11,22)
print_params(10)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [33, 'Паттерны?', False]
values_dict = {"a": 2, "b": 'текст', "c": False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [2, 1]
print_params(*values_list_2, 42)
