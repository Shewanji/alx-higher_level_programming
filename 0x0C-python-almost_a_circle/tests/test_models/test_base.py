#!usr/bin/python3

import unittest
from models.base import Base
from models.square import Square
import json

""" Test cases for the base module """


class BaseTestCase(unittest.TestCase):

    def test_id_assignment_when_id_provided(self):
        """ Test that the provided id is assigned to the instance """
        instance = Base(id=10)
        self.assertEqual(instance.id, 10)

    def test_id_assignment_when_id_not_provided(self):
        """ Test that the id is automatically assigned
        based on the number of objects """
        instance1 = Base()
        instance2 = Base()
        self.assertEqual(instance1.id, 1)
        self.assertEqual(instance2.id, 2)

    def test_id_assignment_across_subclasses(self):
        """ Test that the id counter is shared among subclasses """
        class Child(Base):
            pass

        instance1 = Base()
        instance2 = Child()
        instance3 = Base()

        self.assertEqual(instance1.id, 1)
        self.assertEqual(instance2.id, 1)
        self.assertEqual(instance3.id, 2)


if __name__ == '__main__':
    unittest.main()
