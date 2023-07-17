#!usr/bin/python3

import unittest
from models.square import Square
from io import StringIO
from unittest.mock import patch
"""Test cases for the square modele"""


class SquareTestCase(unittest.TestCase):

    def test_attributes(self):
        # Test that the attributes are correctly assigned
        square = Square(size=5, x=2, y=3)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_id_inherited_from_base(self):
        # Test that the id is correctly inherited from the Base class
        square1 = Square(size=5)
        square2 = Square(size=5)
        self.assertEqual(square1.id, 1)
        self.assertEqual(square2.id, 2)

    def test_valid_size(self):
        # Test that the size must be greater than 0 and an integer
        with self.assertRaises(ValueError):
            Square(size=-5)
        with self.assertRaises(ValueError):
            Square(size=5.5)
        with self.assertRaises(ValueError):
            Square(size="5")

    def test_area(self):
        # Test the area calculation
        square = Square(size=5)
        self.assertEqual(square.area(), 25)

        square = Square(size=8)
        self.assertEqual(square.area(), 64)

    def test_display(self):
        # Test the display method
        square = Square(size=3)

        expected_output = "###\n" \
                          "###\n" \
                          "###\n"

        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            square.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_str(self):
        # Test the string representation
        square = Square(size=5, x=2, y=3)
        expected_output = "[Square] (1) 2/3 - 5"
        self.assertEqual(str(square), expected_output)


if __name__ == '__main__':
    unittest.main()
