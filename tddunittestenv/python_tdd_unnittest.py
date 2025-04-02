# Importing the test module
import unittest


# Function to be tested


def multiplyall(a, b):
    # Check if both inputs are numeric
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numeric.")

    return a * b


# Unit test class
class TestMultiplyAll(unittest.TestCase):

    # Test multiplication of two positive numbers
    def test_positive_numbers(self):
        self.assertEqual(multiplyall(2, 3), 6)

    # Test multiplication involving a negative number
    def test_negative_numbers(self):
        self.assertEqual(multiplyall(-2, 3), -6)
        self.assertEqual(multiplyall(3, -2), -6)
        self.assertEqual(multiplyall(-3, -3), 9)

    # Test multiplication involving zero
    def test_zero(self):
        self.assertEqual(multiplyall(0, 5), 0)
        self.assertEqual(multiplyall(5, 0), 0)
        self.assertEqual(multiplyall(0, 0), 0)

    # Test multiplication of floating-point numbers
    def test_floats(self):
        self.assertEqual(multiplyall(2.5, 4), 10.0)
        self.assertEqual(multiplyall(-2.5, 4), -10.0)
        self.assertEqual(multiplyall(2.5, -4), -10.0)
        self.assertEqual(multiplyall(-2.5, -4), 10.0)

    # Test cases for invalid inputs (strings, None, lists, etc.)
    def test_invalid_string_input(self):
        with self.assertRaises(ValueError):
            multiplyall("a", 4)

    def test_invalid_mixed_input(self):
        with self.assertRaises(ValueError):
            multiplyall(3, "b")

    def test_invalid_none_input(self):
        with self.assertRaises(ValueError):
            multiplyall(None, 5)

    def test_invalid_list_input(self):
        with self.assertRaises(ValueError):
            multiplyall([1, 2], 3)

    def test_invalid_dict_input(self):
        with self.assertRaises(ValueError):
            multiplyall({"key": "value"}, 3)


# Run tests
if __name__ == '__main__':
    unittest.main()
