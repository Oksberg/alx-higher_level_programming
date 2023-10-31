#!/usr/bin/python3
"""Creates a Rectangle object."""


class Rectangle:
    """Represents a Rectangle object with two attributes.

    Attributes:
        width: This is the length of the width and it is private.
        height: This is the length of the height and it is private.
    """
    def __init__(self, width=0, height=0):
        """Initializes the rectangle with eidth and heigth attributes
        Args:
            width (int): The width defaults to 0 if not provided
            height (int): The height defaults to 0 if not provided
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width.

        Must be an integer, otherwise raise TypeError.
        Must be positive, otherwise raise ValueError.
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
        """Retrieves the height.

        Must be an integer, else raise TypeError.
        Must be positive, else raise ValueError.
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
