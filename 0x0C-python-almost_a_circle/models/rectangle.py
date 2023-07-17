#!/usr/bin/python3

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class representing a rectangle object.

    Attributes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x (int): x-coordinate of the rectangle's position.
        y (int): y-coordinate of the rectangle's position.
        id (int): ID of the rectangle.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None):
        Class constructor to initialize the rectangle instance.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): Width value to be set.

        Raises:
            ValueError: If the width is not a positive integer.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): Height value to be set.

        Raises:
            ValueError: If the height is not a positive integer.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x-coordinate of the rectangle's position.

        Args:
            value (int): x-coordinate value to be set.

        Raises:
            ValueError: If the x-coordinate is not a non-negative integer.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y-coordinate of the rectangle's position.

        Args:
            value (int): y-coordinate value to be set.

        Raises:
            ValueError: If the y-coordinate is not a non-negative integer.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Rectangle instance based on the arguments.

        Args:
            *args: Variable number of arguments in the order of
            id, width, height, x, y.
            **kwargs: Variable number of key-worded arguments.
        """
        if len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The calculated area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Print the Rectangle instance with '#' characters
        to represent the shape.
        """
        print("\n" * self.__y, end="")
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        Return a string representation of the Rectangle instance.

        Returns:
            str: A string representation of the Rectangle instance.
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

    def to_dictionary(self):
        """
        Return the dictionary representation of the Rectangle instance.

        Returns:
            dict: A dictionary representing the Rectangle instance with
            attributes id, width, height, x, y.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
