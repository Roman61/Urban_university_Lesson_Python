import random


def is_prime(func):
    def __is_prime(n, k=5):
        # Тест Ферма
        if n <= 1:
            return False
        for _ in range(k):
            a = random.randint(1, n - 1)
            if pow(a, n - 1, n) != 1:
                return False
            return True

    def wrapper(*args, **kwargs):
        return_value = func(*args, **kwargs)
        test = lambda y: 'Простое' if __is_prime(y) else 'Составное'
        print(str(test(return_value)))
        return return_value

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
