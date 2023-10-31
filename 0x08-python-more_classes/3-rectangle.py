#!/usr/bin/python3
"""Creates a class Rectangle"""


class Rectangle:
    """This is a class Rectangle with attributes.

    Attributes:
        width: This is the length of the width and it is private.
        height: This is the length of the height and it is private.
    """

    def __init__(self, width=0, height=0):
        """Initializes the rectangle with width and height as attributes.
        Args:
            width: The rectangle must have a width but defaults to 0
            height: Value must be specified but defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """The width is retrieved here.

        The width must be an integer, otherwise, raise a TypeError.
        It must also be a positive, otherwise, raise a ValueError
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """The height is retrieved here.

        The height must be an integer, otherwise, raise a TypeError.
        It must also be a positive, otherwise, raise a ValueError
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """A method that returns the area."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        if self.__width != 0 and self.__height != 0:
            rectangle = ""
            for i in range(self.__width):
                for j in range(self.__height):
                    rectangle += "#"
                rectangle += "\n"
            return rectangle
        else:
            return ""
