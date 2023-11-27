from CarparkManagementCenter import *
from Car import *


if __name__ == "__main__":
    car_inventory = CarInventory()
    random_car = RandomCar(car_inventory)
    print(random_car.get_car_details())
    print(random_car.get_car_details())
    print(random_car.get_car_details())
    print(random_car.get_car_details())
    manager = CarParkManagementCentre()

    # Load car parks from the JSON file
    try:
        manager.load_from_file("../data/carpark.json")
        print("Carpark data loaded successfully.")
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")

    # Now list all carparks
    manager.list_carparks()
