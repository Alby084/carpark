import json

from abc import ABC, abstractmethod
from datetime import datetime
import random
from json import JSONDecodeError

from Car import *


# https://blog.teclado.com/python-abc-abstract-base-classes/
class Sensor(ABC):
    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def process_car(self):
        pass

    def json_read(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except JSONDecodeError:
            return []  # Return an empty list if the file is empty or not properly formatted

    def json_write(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)


class EnterSensor(Sensor):
    def __init__(self, file_path):
        super().__init__(file_path)

    def process_car(self):
        car_inventory = CarInventory()
        random_car = RandomCar(car_inventory)
        selected_car = random_car.get_car_details()
        cars = self.json_read()
        cars.append(selected_car)
        self.json_write(cars)
        return f"ENTER | {selected_car}"


class ExitSensor(Sensor):
    def __init__(self, file_path, current_cars_path):
        super().__init__(file_path)
        self.current_cars_path = current_cars_path

    def process_car(self):
        current_cars = self.json_read()
        if not current_cars:
            return "NO CARS HAVE LEFT."

        left_car = random.choice(current_cars)
        exit_time = datetime.now().strftime("%d/%m/%Y %I:%M%p")
        left_car_string = f"{left_car} | EXIT AT {exit_time}"

        # Update current cars
        updated_cars = [car for car in current_cars if car != left_car]
        self.json_write(updated_cars)

        # Update exited cars
        exit_cars = self.json_read()
        exit_cars.append(left_car)
        exit_cars.remove(left_car)
        self.json_write(exit_cars)
        return left_car_string


if __name__ == "__main__":
    enter_sensor = EnterSensor("../data/current_cars.json")
    exit_sensor = ExitSensor("../data/exit_cars.json", "../data/current_cars.json")

    # car enter
    print(enter_sensor.process_car())

    # car exit
    print(exit_sensor.process_car())
