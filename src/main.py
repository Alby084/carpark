from CarparkManagementCenter import CarParkManagementCenter
from Car import RandomCar
from Car_list import CarInventory
from Sensors import EnterSensor, ExitSensor


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


if __name__ == "__main__":
    printcarparks()
