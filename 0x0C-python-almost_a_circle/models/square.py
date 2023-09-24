#!/usr/bin/python3
"""Creates a class Square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes attributes for the Square.

        Attributes:
            size (int): The length of the size of the Square.
            x (int): The x coordinate inherited from Rectangle.
            y (int): The y coordinate inherited from Rectangle.
            id (int): id inherited from Rectangle.
        """

        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieves size.
        Checks if size is a non-zero positive integer."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def validate_x(self, value):
        """Calls inherited x getter and setter."""
        self.__x = x

    def validate_y(self, value):
        """Calls inherited x getter and setter."""
        self.__y = y

    def __str__(self):
        """Returns a string rep of the Square"""
        id = self.id
        x = self.x
        y = self.y
        size = self.width
        size = self.height
        return f"[Square] ({id}) {x}/{y} - {size}"
