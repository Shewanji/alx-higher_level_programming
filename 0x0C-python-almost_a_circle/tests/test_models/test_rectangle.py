#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch

""" Test cases for the Rectangle module """


class RectangleTestCase(unittest.TestCase):

    def test_attributes(self):
        """ Test that the attributes are correctly assigned """
        rect = Rectangle(width=5, height=10, x=2, y=3)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)

    def test_id_inherited_from_base(self):
        """ Test that the id is correctly inherited from the Base class """
        rect1 = Rectangle(width=5, height=10)
        rect2 = Rectangle(width=5, height=10)
        self.assertEqual(rect1.id, 1)
        self.assertEqual(rect2.id, 2)

    def test_valid_width(self):
        """ Test that the width must be greater than 0 and an integer """
        with self.assertRaises(ValueError):
            Rectangle(width=-5, height=10)
        with self.assertRaises(TypeError):
            Rectangle(width=5.5, height=10)
        with self.assertRaises(TypeError):
            Rectangle(width="5", height=10)

    def test_valid_height(self):
        """ Test that the height must be greater than 0 and an integer """
        with self.assertRaises(ValueError):
            Rectangle(width=5, height=-10)
        with self.assertRaises(TypeError):
            Rectangle(width=5, height=10.5)
        with self.assertRaises(TypeError):
            Rectangle(width=5, height="10")

    def test_valid_x(self):
        """ Test that x must be non-negative and an integer """
        with self.assertRaises(ValueError):
            Rectangle(width=5, height=10, x=-2)
        with self.assertRaises(TypeError):
            Rectangle(width=5, height=10, x=2.5)
        with self.assertRaises(TypeError):
            Rectangle(width=5, height=10, x="2")

    def test_valid_y(self):
        """ Test that y must be non-negative and an integer """
        with self.assertRaises(ValueError):
            Rectangle(width=5, height=10, y=-3)
        with self.assertRaises(TypeError):
            Rectangle(width=5, height=10, y=3.5)
        with self.assertRaises(TypeError):
            Rectangle(width=5, height=10, y="3")

    def test_area(self):
        """ Test the area calculation"""
        rect = Rectangle(width=5, height=10)
        self.assertEqual(rect.area(), 50)

        rect = Rectangle(width=8, height=4)
        self.assertEqual(rect.area(), 32)

    def test_display(self):
        """ Test the display method"""
        rect = Rectangle(width=3, height=2)

        expected_output = "###\n" \
                          "###\n"

        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            rect.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_str(self):
        """ Test the string representation """
        rect = Rectangle(width=5, height=10, x=2, y=3)
        expected_output = "[Rectangle] (1) 2/3 - 5/10"
        self.assertEqual(str(rect), expected_output)

    def test_update_args(self):
        # Test the update method with no-keyword arguments
        rect = Rectangle(width=5, height=10, x=2, y=3)
        rect.update(2, 8, 12, 4, 6)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.height, 12)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 6)

    def test_update_kwargs(self):
        # Test the update method with key-worded arguments
        rect = Rectangle(width=5, height=10, x=2, y=3)
        rect.update(id=2, width=8, height=12, x=4, y=6)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.height, 12)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 6)

    def test_update_args_kwargs(self):
        """ Test the update method with a combination of
        arguments and key-worded arguments"""
        rect = Rectangle(width=5, height=10, x=2, y=3)
        rect.update(2, width=8, height=12, x=4, y=6)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.height, 12)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 6)

    def test_update_empty_args_kwargs(self):
        # Test the update method with no arguments or key-worded arguments
        rect = Rectangle(width=5, height=10, x=2, y=3)
        rect.update()
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)

    def test_update_invalid_kwargs(self):
        # Test the update method with invalid key-worded arguments
        rect = Rectangle(width=5, height=10, x=2, y=3)
        with self.assertRaises(AttributeError):
            rect.update(invalid_key=5)

    def test_update_args_override_kwargs(self):
        # Test the update method with arguments overriding key-worded arguments
        rect = Rectangle(width=5, height=10, x=2, y=3)
        rect.update(2, 8, 12, x=4, y=6)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.height, 12)
        # x remains unchanged (4 is overridden by the argument)
        self.assertEqual(rect.x, 2)
        # y remains unchanged (6 is overridden by the argument)
        self.assertEqual(rect.y, 3)


if __name__ == '__main__':
    unittest.main()
