import random
import json
from CarparkManagementCenter import CarParkManagementCenter


class ParkingSpaceTracker:
    def __init__(self, carpark):
        self.carpark = carpark

    def find_empty_spots(self):
        return [i for i, space in enumerate(self.carpark.data) if space == "Empty"]

    def park_car(self, car):
        empty_spots = self.find_empty_spots()
        if empty_spots:
            empty_spot_index = random.choice(empty_spots)
            self.carpark.data[empty_spot_index] = car
            return True
        return False

    def leave_car(self):
        occupied_spots = [i for i, space in enumerate(self.carpark.data) if space != "Empty"]
        if occupied_spots:
            spot_to_leave = random.choice(occupied_spots)
            leaving_car = self.carpark.data[spot_to_leave]
            self.carpark.data[spot_to_leave] = "Empty"
            return leaving_car
        return None

    def display_parking_spaces(self):
        for i, space in enumerate(self.carpark.data):
            status = space if space != "Empty" else "Empty"
            print(f"Space {i + 1}: {status}")


class CarManager:
    def __init__(self, file_path):
        self.file_path = file_path
        with open(file_path, 'r') as file:
            self.car_data = json.load(file)

    def get_available_cars(self, parked_cars):
        return [car for car in self.car_data if car not in parked_cars]

    def choose_random_car(self, available_cars):
        return random.choice(available_cars) if available_cars else "Empty"

    def remove_car(self, car):
        if car in self.car_data:
            self.car_data.remove(car)
            with open(self.file_path, 'w') as file:
                json.dump(self.car_data, file, indent=4)

    def log_exit_car(self, car):
        exit_cars_file_path = "../data/exit_cars.json"
        try:
            with open(exit_cars_file_path, 'r') as file:
                exit_cars = json.load(file)
        except FileNotFoundError:
            exit_cars = []

        exit_cars.append(car)

        with open(exit_cars_file_path, 'w') as file:
            json.dump(exit_cars, file, indent=4)


class Display:
    def __init__(self, carpark, car_manager):
        self.tracker = ParkingSpaceTracker(carpark)
        self.car_manager = car_manager

    def update_display(self):
        available_cars = self.car_manager.get_available_cars(self.tracker.carpark.data)
        self.randomcar = self.car_manager.choose_random_car(available_cars)
        if self.randomcar != "Empty":
            parked = self.tracker.park_car(self.randomcar)
            if not parked:
                self.car_manager.remove_car(self.randomcar)
                self.car_manager.log_exit_car(self.randomcar)
                return print(f"\nFULL {self.randomcar} EXIT")

        # Display current parking space status
        print("\nCurrent Parking Spaces Status:")
        self.tracker.display_parking_spaces()

        print(f"\nPARKED {self.randomcar}")

    def car_leaves(self):
        leaving_car = self.tracker.leave_car()
        if leaving_car:
            self.car_manager.remove_car(leaving_car)
            self.car_manager.log_exit_car(leaving_car)
            return print(f"UNPARKED {leaving_car}")
        else:
            print("NO PARKED CARS")


if __name__ == "__main__":
    car_manager = CarManager("../data/current_cars.json")

    carpark_manager = CarParkManagementCenter()

    # Read car park data from carpark.json and add carparks to manager
    with open("../data/carpark.json", "r") as file:
        carpark_data = json.load(file)
        for carpark in carpark_data:
            carpark_manager.add_carpark(carpark["carpark_name"], carpark["carpark_spaces"], carpark["carpark_temp"])

    carpark_manager.list_carparks()

    # Select carpark
    selected_carpark = carpark_manager.car_parks[0]

    # Display
    # Display(selected_carpark, car_manager)
    # Display(selected_carpark, car_manager).update_display()

    # Car leave
    # Display(selected_carpark, car_manager).car_leaves()
