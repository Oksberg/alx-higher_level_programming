#!/usr/bin/python3
"""Create a class Square"""


class Square:
    """A representation of a real world square.

    This Square object has only one attribute now

    Attribute:
        size: The length of the sides of the square.

    """

    def __init__(self, size):
        """This __init__ method initializes the class with the attribute size.

        Args:
            param1 (size): The size of the sides.

        """
        self.__size = size
