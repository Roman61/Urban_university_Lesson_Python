class House:
    numberOfFloors = 10

    def viewer(self):
        for atr in dir(self):
            if atr[:2] == '__' and atr[-2:] == '__':
                continue
            if isinstance(getattr(House, atr), int):
                print(f'Текущий этаж равен: {getattr(House, atr)}')


house = House()
house.viewer()
