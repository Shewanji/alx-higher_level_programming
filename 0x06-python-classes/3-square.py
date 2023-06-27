#!/usr/bin/python3
""" This ensures that the file will be exucutable
class Square that defines a square by: (based on 2-square.py) """


class Square:
    """
    A class representing a square.

    Attributes:
        __size (int): The size of the square (private instance attribute).
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance with an optional size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates and returns the current area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
