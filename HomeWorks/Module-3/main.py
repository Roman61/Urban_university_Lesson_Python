def test(*args, **kwargs):
    values = kwargs.copy()
    i = 0
    count = len(args)
    while i < count:
        values[str(i)] = args[i]
        i += 1
    for key, value in values.items():
        print(key, value)


params_name = {"a": 4, "b": True, "c": "Name"}
params_index = ["text", 111, False]
test(*params_index, **params_name)
test(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
test("HTML_DOM?", "HTML_DOM?", "HTML_DOM?", "HTML_DOM?", "HTML_DOM?", "HTML_DOM?", "HTML_DOM?", "HTML_DOM?", )


def n_factorial(n):
    if n == 0:
        return 1
    else:
        return n * n_factorial(n - 1)


print(n_factorial(5))
