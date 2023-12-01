import unittest
from datetime import datetime
from src.Car import NumberPlatePicker, DateGenerator  # Replace 'your_module' with the actual name of your module
from src.CarparkManagementCenter import CarParkManagementCenter

class Unittests(unittest.TestCase):

    def test_number_plate_length(self):
        number_plate_picker = NumberPlatePicker()
        number_plate = number_plate_picker.get_numberplate()
        self.assertEqual(len(number_plate), 7)

    def test_number_plate_content(self):
        number_plate_picker = NumberPlatePicker()
        number_plate = number_plate_picker.get_numberplate()
        self.assertTrue(all(char.isupper() or char.isdigit() for char in number_plate))

    def test_get_current_date(self):
        # Get current date time
        expected_date = datetime.now().strftime("%d/%m/%Y %I:%M%p")

        # Get date
        generated_date = DateGenerator.get_current_date()

        # Tests if the generated date is close to system date
        # Allowing a small margin for execution time
        # Suggested by chatgpt
        self.assertTrue(abs(datetime.strptime(generated_date, "%d/%m/%Y %I:%M%p") - datetime.strptime(expected_date,
                                                                                                      "%d/%m/%Y %I:%M%p")).seconds < 5)

    def test_add_carpark(self):
        manager = CarParkManagementCenter()
        manager.add_carpark("Test", 11, 11.1)

        self.assertEqual(len(manager.car_parks), 1)
        self.assertEqual(manager.car_parks[0].carpark_name, "Test")
        self.assertEqual(manager.car_parks[0].carpark_spaces, 11)
        self.assertEqual(manager.car_parks[0].carpark_temp, 11.1)


if __name__ == '__main__':
    unittest.main()
