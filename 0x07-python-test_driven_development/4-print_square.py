#!/usr/bin/python3
"""

This module contain a function that prints a square with the character #.

"""


def print_square(size):
    '''This function prints a square with the character #

    Args:
        size (int): The size length of the square

    Raises:
        TypeError: If size is not an integer or float
        ValueError: If size is less than 0

    '''
    if isinstance(size, int):
        if size < 0:
            raise ValueError("size must be >= 0")
        for _ in range(size):
            print('#' * size)
    elif isinstance(size, float):
        raise TypeError("size must be an integer")
    else:
        raise TypeError("size must be an integer")
