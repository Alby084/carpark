from CarparkManagementCenter import CarParkManagementCenter
from Sensors import EnterSensor, ExitSensor
from Display import CarManager, Display
from time import sleep
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


def randomselector():
    return random.randint(0, 4)


def wait():
    return sleep(random.randint(5, 10))


if __name__ == "__main__":

    carpark_manager = CarParkManagementCenter()

    # Read car park data from carpark.json and add carparks to manager
    with open("../data/carpark.json", "r") as file:
        carpark_data = json.load(file)
        for carpark in carpark_data:
            carpark_manager.add_carpark(carpark["carpark_name"], carpark["carpark_spaces"], carpark["carpark_temp"])

    carpark_manager.list_carparks()
    repeat2 = True

    while repeat2:
        try:
            carpark = int(input("select carpark as number: "))
        except ValueError:
            print("Error input must be a number.")
            continue
        if carpark > 2 or carpark <= 0:
            print("Error input must be a valid number")
        else:
            repeat2 = False

    # Select carpark
    selected_carpark = carpark_manager.car_parks[carpark - 1]

    # Car leave
    # Display(selected_carpark, car_manager).car_leaves()

    repeat = True
    carenter()
    wait()
    carenter()
    wait()
    carenter()
    car_manager = CarManager("../data/current_cars.json")
    wait()
    Display(selected_carpark, car_manager).update_display()
    Display(selected_carpark, car_manager)
    wait()
    Display(selected_carpark, car_manager).update_display()
    Display(selected_carpark, car_manager)
    wait()
    Display(selected_carpark, car_manager).update_display()
    Display(selected_carpark, car_manager)
    wait()
    Display(selected_carpark, car_manager).car_leaves()
    sleep(2)
    carexit()
    wait()
    carenter()
    car_manager = CarManager("../data/current_cars.json")
    wait()
    Display(selected_carpark, car_manager).update_display()
    Display(selected_carpark, car_manager)
    wait()
    Display(selected_carpark, car_manager).car_leaves()
    sleep(2)
    carexit()
    wait()
    carenter()
    wait()
    carenter()
    wait()
    carenter()
    car_manager = CarManager("../data/current_cars.json")

    while repeat:
        status = randomselector()
        match status:
            case 1:
                # Display
                wait()
                Display(selected_carpark, car_manager).update_display()
                Display(selected_carpark, car_manager)
            case 2:
                # Car leave
                wait()
                Display(selected_carpark, car_manager).car_leaves()
            case 3:
                wait()
                carenter()
                car_manager = CarManager("../data/current_cars.json")
            case 4:
                wait()
                carexit()
