import random
import string
from datetime import datetime

# Assuming CarInventory is defined elsewhere
from Car_list import CarInventory


class ModelPicker:
    """ Picks a random model from the car inventory. """

    def __init__(self, car_inventory):
        self.car_inventory = car_inventory

    def pick_random_model(self):
        return random.choice(self.car_inventory.cars)


class NumberPlatePicker:
    """ Generates a random number plate. """

    def __init__(self):
        self.numberplate = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))

    def get_numberplate(self):
        return self.numberplate


class DateGenerator:
    """ Generates the current date and time. """

    @staticmethod
    def get_current_date():
        return datetime.now().strftime("%d/%m/%Y %I:%M%p")


class Car:
    """ Represents a car with a number plate, entry and exit dates, and a model. """

    def __init__(self, model, number_plate, date_enter, date_exit=None):
        self.model = model
        self.number_plate = number_plate
        self.date_enter = date_enter
        self.date_exit = date_exit


class RandomCar:
    """ Generates a random car each time car details are requested. """

    def __init__(self, car_inventory):
        self.car_inventory = car_inventory

    def get_car_details(self):
        model_picker = ModelPicker(self.car_inventory)
        number_plate = NumberPlatePicker().get_numberplate()
        date_enter = DateGenerator.get_current_date()
        car = Car(
            model=model_picker.pick_random_model(),
            number_plate=number_plate,
            date_enter=date_enter
        )
        return f"[Car: {car.model} | Number plate: {car.number_plate} | Entered: {car.date_enter}]\n"


# Example usage
if __name__ == "__main__":
    car_inventory = CarInventory()  # Assuming this is defined elsewhere
    random_car = RandomCar(car_inventory)
    print(random_car.get_car_details())
    print(random_car.get_car_details())
    print(random_car.get_car_details())
