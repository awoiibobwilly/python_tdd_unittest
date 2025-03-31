# importing the test library
import unittest


# Refactoring the logic function for the first time
def multiplyall(a, b):
    return 1


# Test cases for multiplyall function, beginning of Test Suite
class TestMultiplyAll(unittest.TestCase):

    def test_multiplyall1(self):
        self.assertEqual(multiplyall(1, 1), 1)

    def test_multiplyall2(self):
        self.assertEqual(multiplyall(2, 2), 4)


if __name__ == '__main__':
    unittest.main()
# End of test suite
