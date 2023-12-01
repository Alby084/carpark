import random
import json


class CarPark:
    def __init__(self, carpark_name: str, carpark_spaces: int, carpark_temp: float = None):
        self.carpark_name = carpark_name
        self.carpark_spaces = carpark_spaces
        self.carpark_temp = carpark_temp if carpark_temp is not None else round(random.uniform(15, 45), 2)
        self.data = ["Empty"] * carpark_spaces

    def __str__(self):
        return f"Name: {self.carpark_name} | Spaces: {self.carpark_spaces} | Temperature: {self.carpark_temp}°C"


class CarParkManagementCenter:
    def __init__(self):
        self.car_parks = []

    def add_carpark(self, carpark_name: str, carpark_spaces: int, carpark_temp: float = None):
        carpark = CarPark(carpark_name, carpark_spaces, carpark_temp)
        self.car_parks.append(carpark)

    def list_carparks(self):
        for carpark in self.car_parks:
            print(carpark)

    def save_to_file(self, filename):
        carpark_data = [
            {
                "carpark_name": carpark.carpark_name,
                "carpark_spaces": carpark.carpark_spaces,
                "carpark_temp": carpark.carpark_temp
            } for carpark in self.car_parks
        ]
        with open(filename, "w") as file:
            json.dump(carpark_data, file, indent=4)

    def load_from_file(self, filename):
        with open(filename, "r") as file:
            carpark_data = json.load(file)
            for carpark in carpark_data:
                self.add_carpark(carpark["carpark_name"], carpark["carpark_spaces"], carpark["carpark_temp"])


if __name__ == "__main__":
    manager = CarParkManagementCenter()

    # Add carpark with random temperature
    manager.add_carpark("Moondalup Large", 50)
    manager.add_carpark("Moondalup Small", 10)

    # save the current state of the list to file
    try:
        manager.save_to_file("../data/carpark.json")
        print("Carpark data saved successfully.")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")

    # List all carparks
    manager.list_carparks()
