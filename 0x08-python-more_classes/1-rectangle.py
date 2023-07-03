#!/usr/bin/python3
"""This module defines a rectangle by: (based on 0-rectangle.py)"""


class Rectangle:
    """represents a rectangle"""

    def __init__(self, width=0, height=0):
        """initialize rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """get width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value: int):
        """set the width of the rectangle"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """get height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value: int):
        """set the height of the rectangle"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
