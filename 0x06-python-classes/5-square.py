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
        self.__size = size

    def area(self):
        """area: This method calculates and returns
        the area of the Square object
        """
        return (self.__size ** 2)

    def my_print(self):
        """my_print: Prints the Square object to stdout.
        It prints an empty line if size is 0.
        """
        if self.__size != 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
        print()

    @property
    def size(self):
        """size: Is the length of the sides of the Square object.

        The attribute 'size' should always be an integer and must not
        be negative.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
