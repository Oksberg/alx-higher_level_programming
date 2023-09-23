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
