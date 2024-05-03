data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


# "А есть ли универсальное решение для подсчёта суммы всех чисел и длин всех строк?"
def tree_summator(structure, a):
    if not structure:
        return a
    else:
        for i in structure:
            if type(i) == str:
                a += len(i)
            elif type(i) == int:
                a += i
            elif type(i) == dict:
                a = tree_summator(i.values(), a)
            else:
                a = tree_summator(i, a)
    return a


a = tree_summator(data_structure, 0)
print(a)
