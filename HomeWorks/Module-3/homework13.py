# 3.
# Красный, синий и желтый называются основными цветами, потому что их нельзя получить путем смешения других цветов.
# При смешивании двух основных цветов получается вторичный цвет:
#
#  -если смешать красный и синий, то получится фиолетовый;
#  -если смешать красный и желтый, то получится оранжевый;
#  -если смешать синий и желтый, то получится зеленый.
#
# Напишите программу, которая считывает названия двух основных цветов для смешивания. Если пользователь вводит
# что-нибудь помимо названий «красный», «синий» или «желтый», то программа должна вывести сообщение об ошибке.
# В противном случае программа должна вывести название вторичного цвета, который получится в результате.
#
# a,b = красный, синий
# result —> фиолетовый
def colors(color_first, color_second):
    str_test = '«красный», «синий» или «желтый»'
    if str_test.__contains__(color_first) and str_test.__contains__(color_second):
        if color_first == 'красный' and color_second == 'синий' or color_first == 'синий' and color_second == 'красный':
            return 'фиолетовый'
        elif color_first == 'красный' and color_second == 'желтый' or color_first == 'желтый' and color_second == 'красный':
            return 'оранжевый'
        elif color_first == 'синий' and color_second == 'желтый' or color_first == 'желтый' and color_second == 'синий':
            return 'зеленый'
        elif color_first == color_second:
            return color_first
        else:
            print('Что-то пошло не так')
    else:
        print('Что-то пошло не так')


def test():
    print('test: ', end='\t')
    tuple_ = {"фиолетовый": "красный, синий", "оранжевый": "красный, желтый", 'зеленый': "синий, желтый"}
    list_ = ['красный', 'синий', 'желтый']
    for i in list_:
        for j in list_:
            if j != i:
                if (str(tuple_[colors(i, j)])).__contains__(i) and (str(tuple_[colors(i, j)])).__contains__(j):
                    pass
                else:
                    print('Тест не прошёл')
                    exit()
    print("Ок")


test()
print('Красный, синий и желтый называются основными цветами,')
print(' потому что их нельзя получить путем смешения других цветов.')
color_first_input, color_second_input = input("Введите цвета, через запятую: ").split(",")
print("Результат: ", colors(color_first_input.lower().strip(), color_second_input.lower().strip()))

# Основные цвета RGB!!!



