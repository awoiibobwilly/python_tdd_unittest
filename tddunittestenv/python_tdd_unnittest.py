# importing the test library
import unittest


def multiplyall(a, b):
    return a * b


# Test cases for multiplyall function, beginning of Test Suite
class TestMultiplyAll(unittest.TestCase):

    def test_multiplyall1(self):
        self.assertEqual(multiplyall(1, 1), 2)


if __name__ == '__main__':
    unittest.main()
# End of test suite
