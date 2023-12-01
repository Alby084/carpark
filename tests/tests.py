import unittest
from datetime import datetime
from src.Car import NumberPlatePicker, DateGenerator  # Replace 'your_module' with the actual name of your module


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


if __name__ == '__main__':
    unittest.main()
