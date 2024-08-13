import unittest
from random_utils import generate_random_numbers

class TestGenerateRandomNumbers(unittest.TestCase):
    
    def test_generate_correct_amount(self):
        """Test that the correct amount of numbers is generated."""
        result = generate_random_numbers(10, 2, 1000)
        self.assertEqual(len(result), 10)

    def test_numbers_divisible_by_step(self):
        """Test that all generated numbers are divisible by the step."""
        step = 5
        result = generate_random_numbers(10, step, 1000)
        for number in result:
            self.assertEqual(number % step, 0)

    def test_invalid_amount(self):
        """Test that a ValueError is raised for invalid amount."""
        with self.assertRaises(ValueError) as context:
            generate_random_numbers(0, 2, 1000)
        self.assertEqual(str(context.exception), "Amount must be a positive integer.")

    def test_invalid_step(self):
        """Test that a ValueError is raised for invalid step."""
        with self.assertRaises(ValueError) as context:
            generate_random_numbers(10, 0, 1000)
        self.assertEqual(str(context.exception), "Step must be a positive integer.")

    def test_default_parameters(self):
        """Test with default parameters for validity."""
        result = generate_random_numbers(100, 2, 1000)
        self.assertEqual(len(result), 100)
        for number in result:
            self.assertEqual(number % 2, 0)

if __name__ == '__main__':
    unittest.main()
