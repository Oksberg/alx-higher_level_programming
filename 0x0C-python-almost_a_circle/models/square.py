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

        super().__init__(size, size, x, y, id)

    def validate_width(self, size):
        """Calls inherited width getter and setter."""
        self.__width = size

    def validate_width(self, size):
        """Calls inherited height getter and setter."""
        self.__height = size

    def validate_x(self, value):
        """Calls inherited x getter and setter."""
        self.__x = x

    def validate_x(self, value):
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
