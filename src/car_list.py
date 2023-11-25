# car_class.py

class CarInventory:
    def __init__(self):
        file_path = "../data/car_types.txt"
        self.cars = self._read_car_types(file_path)

    @staticmethod
    def _read_car_types(file_path):
        with open(file_path, 'r') as file:
            car_types = file.read().split(',')
            car_types = [car.strip() for car in car_types]
        return car_types
