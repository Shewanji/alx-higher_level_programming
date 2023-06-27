#!/usr/bin/python3
""" This ensures that the file will be exucutable
class Square that defines a square by: (based on 5-square.py)"""


class Square:
    """
    A class representing a square.

    Attributes:
        __size (int): The size of the square (private instance attribute).
        __position (tuple): The position of the square
        (private instance attribute).
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance with an optional size and position.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square.
            Defaults to (0, 0).

        Raises:
            TypeError: If the provided size is not an integer.
                     If the provided position is not a tuple of
                     2 positive integers.
            ValueError: If the provided size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If the provided position is not a tuple of
            2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates and returns the current area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character '#' in stdout.

        Prints an empty line if size is equal to 0.
        The position is used to adjust the spacing before printing the square.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
