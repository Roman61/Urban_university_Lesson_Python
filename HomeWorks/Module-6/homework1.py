class Car:
    def __init__(self):
        self.price = 1000000
        self.__horse_power = 570

    def horse_powers(self):
        return self.__horse_power


class Nissan(Car):
    def __init__(self):
        super().__init__()
        self.price = 2400000
        self.__torque = 637
        self.rpm = 4699

    def horse_powers(self):
        return (self.__torque * self.rpm)/5252


class Kia(Car):
    def __init__(self):
        super().__init__()
        self.price = 1400000
        self.__torque = 420
        self.rpm = 3200

    def horse_powers(self):
        return (self.__torque * self.rpm)/5252





