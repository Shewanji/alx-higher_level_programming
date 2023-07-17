#!/usr/bin/python3
"""This module defines a square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Retrieve the size attribute of the Square.

        Returns:
            int: The size of the Square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size attribute of the Square.

        Args:
            value (int): The size value to be set.

        Raises:
            ValueError: If the size is not a positive integer.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Square instance.

        Args:
            *args: List of arguments (no-keyworded) in the order:
            id, size, x, y.
            **kwargs: Dictionary of keyworded arguments where each key
            represents an attribute.

        If *args exists and is not empty, the arguments are assigned
        to the corresponding attributes in the order: id, size, x, y.
        If **kwargs exists, the keyworded arguments are assigned to
        the attributes based on the key-value pairs in the dictionary.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def __str__(self):
        """
        Return a string representation of the Square instance.

        Returns:
            str: A string representation of the Square instance.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        """
        Return the dictionary representation of the Square  instance.

        Returns:
            dict: A dictionary representing the Square instance with
            attributes id, size, x, y.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
