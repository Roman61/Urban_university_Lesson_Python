cars = ["BMW", "MB", "LADA", "KIA", "HONDA"]
cars_count = 0

for i in range(0, len(cars)):
    print('Я езжу на автомабиле марки', cars[i])
    if i >= 2:
        cars_count += 10
pass

