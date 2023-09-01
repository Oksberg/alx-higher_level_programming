#!/usr/bin/python3
"""Create a class Square"""


class Square:
    """A representation of a real world square.

    This Square object has only one attribute now

    Attribute:
        size: The length of the sides of the square.

    """

    def __init__(self, size=0):
        """This __init__ method initializes the class with default
        value of 0 for the attribute size.

        Args:
            param1 (size): The size of the sides.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area: This method calculates and returns the area of the Square object
        """
        return (self.__size ** 2)
