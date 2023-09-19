#!/usr/bin/python3
"""Defines a class Rectangle."""
from models.base import Base


class Rectangle(Base):
    """A representation of a rectangle, a subclass. """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes attributes for the Rectangle.

        Args:
            width (int): The width of the Rectangle, it is required.
            height (int): The height, defaults, it is required.
            x (int): The x-coordinate of the Rectangle, defaults to 0.
            y (int): y-coordinate of the Rectangle, defaults to 0.
            id (int): The identity of the Rectangle.

        Raise:
            TypeError: If any of the inputs is not of type int with
            message '<name of the attribute> must be an integer'.
            ValueError: If width or height is <= 0 with message
            '<name of the attribute> must be > 0'.
            ValueError: If x or y is < 0 with messsage
            '<name of the attribute> must be >= 0'.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieves the width.

        The width is set to be a non-zero poditive integer, it
        raises an exception if it's not.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height.

        The height is set to be a non-zero positive integer, it
        raises an exception if it's not.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieves x.

        x is set to be a positive integer, it raises an exception if
        it's not.
        """
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieves y.

        y is set to be a positive integer, it raises an exception if
        it's not.
        """
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the Rectangle instance."""
        return self.width * self.height

    def display(self):
        """Prints a # rep of the Rectangle to stdout."""
        for i in range(self.width):
            for j in range(self.height):
                print("#", end="")
            print()
        
