from bigO import BigO

# Создаем экземпляр BigO
bigo = BigO()

# Определять функции, которые мы хотим протестировать
def test_function1(n):
    return [i for i in range(n)]  # O(n)

def test_function2(n):
    return [i * 2 for i in range(n)]  # O(n)

# Выполняем тестирование
test_cases = {
    "Test Function 1": test_function1,
    "Test Function 2": test_function2,
}

for name, func in test_cases.items():
    complexities = bigo.test(func, n_values=[10, 100, 1000])
    print(f"{name}: {complexities}")
