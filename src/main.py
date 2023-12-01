from CarparkManagementCenter import CarParkManagementCenter
from Sensors import EnterSensor, ExitSensor
from Display import CarManager, Display
import random
import json


def carenter():
    enter_sensor = EnterSensor("../data/current_cars.json")
    print(enter_sensor.process_car())


def carexit():
    exit_sensor = ExitSensor("../data/exit_cars.json", "../data/current_cars.json")
    print(exit_sensor.process_car())


def printcarparks():
    manager = CarParkManagementCenter()

    # Load carparks from JSON file
    try:
        manager.load_from_file("../data/carpark.json")
        print("Carparks:")
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")

    # list all loaded carparks
    manager.list_carparks()


def randomselector(number):
    number = random.randint(0, 2)


if __name__ == "__main__":
    car_manager = CarManager("../data/current_cars.json")

    carpark_manager = CarParkManagementCenter()

    # Read car park data from carpark.json and add carparks to manager
    with open("../data/carpark.json", "r") as file:
        carpark_data = json.load(file)
        for carpark in carpark_data:
            carpark_manager.add_carpark(carpark["carpark_name"], carpark["carpark_spaces"], carpark["carpark_temp"])

    # Select carpark
    selected_carpark = carpark_manager.car_parks[0]

    # Display
    Display(selected_carpark, car_manager)
    Display(selected_carpark, car_manager)
    Display(selected_carpark, car_manager)

    # Car leave
    # Display(selected_carpark, car_manager).car_leaves()
