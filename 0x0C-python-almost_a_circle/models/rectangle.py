#!/usr/bin/python3
"""Defines a class Rectangle."""


from base import Base


class Rectangle(Base):
    """A representation of a rectangle object. """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes attributes for the Rectangle.

        Attributes:
            width: The width of the Rectangle that defaults to 0
            height: The height, defaults to 0
            x: An attribute of the Rectangle, defaults to 0
            y: An attribute of the Rectangle, defaults to 0
        """

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
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
        elif value <= 0:
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
        elif value <= 0:
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
        elif value < 0:
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
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
