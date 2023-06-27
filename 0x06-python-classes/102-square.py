#!/usr/bin/python3
""" This ensures that the file will be exucutable
class Square that defines a square by: (based on 4-square.py)"""


class Square:
    """
    A class representing a square.

    Attributes:
        __size (float or int): The size of the square
        (private instance attribute).
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance with an optional size.

        Args:
            size (float or int, optional): The size of the square.
            Defaults to 0.

        Raises:
            TypeError: If the provided size is not a number (float or integer).
            ValueError: If the provided size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (float or int): The size of the square.

        Raises:
            TypeError: If the provided size is not a number (float or integer).
            ValueError: If the provided size is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the current area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Checks if two Square instances have equal areas.

        Args:
            other (Square): The other Square instance to compare with.

        Returns:
            bool: True if areas are equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        Checks if two Square instances have unequal areas.

        Args:
            other (Square): The other Square instance to compare with.

        Returns:
            bool: True if areas are unequal, False otherwise.
        """
        return not self.__eq__(other)

    def __gt__(self, other):
        """
        Checks if the area of the current Square instance is greater than
        the area of another Square instance.

        Args:
            other (Square): The other Square instance to compare with.

        Returns:
            bool: True if the area is greater, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """
        Checks if the area of the current Square instance is greater than or
        equal to the area of another Square instance.

        Args:
            other (Square): The other Square instance to compare with.

        Returns:
            bool: True if the area is greater than or equal, False otherwise.
        """
        return self.__gt__(other) or self.__eq__(other)

    def __lt__(self, other):
        """
        Checks if the area of the current Square instance is less
        than the area of another Square instance.

        Args:
            other (Square): The other Square instance to compare with.

        Returns:
            bool: True if the area is less, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """
        Checks if the area of the current Square instance is less than
        or equal to the area of another Square instance.

        Args:
            other (Square): The other Square instance to compare with.

        Returns:
            bool: True if the area is less than or equal, False otherwise.
        """
        return self.__lt__(other) or self.__eq__(other)
