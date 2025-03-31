# importing the test library
import unittest


# The start of the test suite
class TestMultiplyAll(unittest.TestCase):

    def test_multiplyall1(self):
        self.assertEqual(multiplyall(1, 1), 1)


if __name__ == '__main__':
    unittest.main()
# End of test suite