#!/usr/bin/python3
"""
Creates a class Rectangle that inherits from the Base class and is a
super class to the Square class.
"""
from .base import Base


class Rectangle(Base):
    """Represents a Rectangle object that inherents from class
    Base. And has 4 other attributes.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes 4 attributes and inherits 1 from Base.
        Args:
            width: width of the Rectangle
            height: height of the Rectangle
            x: x-coordinate
            y: y-coordinate
            id: inherited from Base
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieves the private attribute width.
        If value is not an integer, a TypeError is raised.
        If value is not a non-zero positive number, a ValueError is
        raised.
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
        """Retrieves the private attribute height.
        If value is not an integer, a TypeError is raised.
        If value is not a non-zero positive number,
        a ValueError is raised.
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
        """Retrieves the private attribute x.
        If value is not an integer, a TypeError is raised.
        If value is negative, a ValueError is raised.
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
        """Retrieves the private attribute y.
        If value is not an integer, a TypeError is raised.
        If value is negative, a ValueError is raised.
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
        """Returns the area of the Rectangle."""

        return self.width * self.height

    def display(self):
        """Prints a string representation of the Rectangle."""

        for n in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.width):
                print("#", end="")
            for m in range(self.x):
                print("", end="")
            print()

    def __str__(self):
        """
        Displays a human-readable representation of the Rectangle.
        """

        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
        f"{self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Assigns arguments and keyword arguments to
        the attributes."""

        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = 3
        if len(args) >= 5:
            self.y = 4

        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns a dictionary representation of a Rectangle."""

        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
