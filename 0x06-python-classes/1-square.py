#!/usr/bin/python3
""" This ensures that the file will be exucutable
 class Square that defines a square by: (based on 0-square.py)"""


class Square:
    """
    A class representing a square.

    Attributes:
        size (int): The size of the square (private instance attribute).
    """

    def __init__(self, size):
        """
        Initializes a Square instance with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
