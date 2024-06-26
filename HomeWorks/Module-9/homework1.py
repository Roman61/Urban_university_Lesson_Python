def is_even(num):
    if num % 2 != 0:
        return True
    else:
        return False


def square(num):
    return num ** 2


arr = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

thinning_arr = list(filter(is_even, arr))
out_arr = list(map(square, thinning_arr))
print("Применение filter и map:\t\t\t\t", out_arr)

#Cписковые, словарные сборки

out_arr_g = [x ** 2 for x in arr if x % 2 != 0]
print("Применение списковые, словарные сборки:\t", out_arr_g)
