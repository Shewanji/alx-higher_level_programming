#!usr/bin/python3
import unittest

max_integer = __import__("6-max_integer").max_integer

"""unittest for max_integer function
"""


class MaxIntegerTest(unittest.TestCase):
    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_positive_numbers(self):
        result = max_integer([1, 2, 3, 4, 5])
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        result = max_integer([-1, -2, -3, -4, -5])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        result = max_integer([-1, 2, -3, 4, -5])
        self.assertEqual(result, 4)

    def test_duplicate_numbers(self):
        result = max_integer([5, 5, 5, 5])
        self.assertEqual(result, 5)

    def test_single_number(self):
        result = max_integer([42])
        self.assertEqual(result, 42)

    def test_large_numbers(self):
        result = max_integer([999999999999, 1000000000000, 999999999998])
        self.assertEqual(result, 1000000000000)

if __name__ == '__main__':
    unittest.main()

