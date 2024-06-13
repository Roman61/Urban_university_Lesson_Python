class Vehicle:
    def __init__(self):
        self.vehicle_type = "none"


class Car:
    def __init__(self):
        super().__init__()
        self.price = 1000000
        self.__horse_power = 570

    def horse_powers(self):
        return self.__horse_power


class Nissan(Car, Vehicle):
    def __init__(self):
        super().__init__()
        self.price = 2400000
        self.__torque = 637
        self.rpm = 4699
        self.vehicle_type = 'Car'

    def horse_powers(self):
        return (self.__torque * self.rpm)/5252


if __name__ == '__main__':
    nissan = Nissan()
    print(nissan.vehicle_type, nissan.price)

