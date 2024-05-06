data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

data_structure_2 = [
    ("А есть ли универсальное решение для подсчёта суммы всех чисел и длин всех строк?", [{(2, 'Urban', ('Urban2', 35))}]),
    [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]],
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
            if str == type(i):
                a += len(i)
            elif int == type(i):
                a += i
            elif dict == type(i):
                a = tree_summator(i.values(), a)
                a = tree_summator(i.keys(), a)
            else:
                a = tree_summator(i, a)
    return a


a = tree_summator(data_structure, 0)
print(a)
