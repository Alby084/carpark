import random
import json
from CarparkManagementCenter import CarParkManagementCentre


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

    def display_parking_spaces(self):
        for i, space in enumerate(self.carpark.data):
            status = space if space != "Empty" else "Empty"
            print(f"Space {i + 1}: {status}")


class CarManager:
    def __init__(self, file_path):
        with open(file_path, 'r') as file:
            self.car_data = json.load(file)

    def get_available_cars(self, parked_cars):
        return [car for car in self.car_data if car not in parked_cars]

    def choose_random_car(self, available_cars):
        return random.choice(available_cars) if available_cars else "No cars available"


class Display:
    def __init__(self, carpark, car_manager):
        self.tracker = ParkingSpaceTracker(carpark)
        self.car_manager = car_manager
        self.update_display()

    def update_display(self):
        available_cars = self.car_manager.get_available_cars(self.tracker.carpark.data)
        self.randomcar = self.car_manager.choose_random_car(available_cars)
        if self.randomcar != "Empty":
            parked = self.tracker.park_car(self.randomcar)
            if not parked:
                print("No empty spots available, car left")

        # Display current parking space status
        print("\nCurrent Parking Spaces Status:")
        self.tracker.display_parking_spaces()

        print(f"\n{self.randomcar}")


if __name__ == "__main__":
    car_manager = CarManager("../data/current_cars.json")

    # Create CarParkManagementCentre instance
    carpark_manager = CarParkManagementCentre()

    # Read car park data from carpark.json and add carparks to manager
    with open("../data/carpark.json", "r") as file:
        carpark_data = json.load(file)
        for carpark in carpark_data:
            carpark_manager.add_carpark(carpark["carpark_name"], carpark["carpark_spaces"], carpark["carpark_temp"])

    # Select carpark
    selected_carpark = carpark_manager.car_parks[0]

    # Create Display instance with selected carpark
    display_instance = Display(selected_carpark, car_manager)
