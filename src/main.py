from abc import ABC
import random
import string
from datetime import datetime
from car_list import CarInventory

class Sensors(ABC):
    pass


class EntrySensor(Sensors):
    pass


class ExitSensor(Sensors):
    pass


class CarparkManagementCenter:
    pass


class Display:
    pass


class Car:
    pass


class Carpark:
    pass


if __name__ == "__main__":
    car_inventory = CarInventory()  # Assuming this is defined elsewhere
    random_car = RandomCar(car_inventory)
    print(random_car.get_car_details())