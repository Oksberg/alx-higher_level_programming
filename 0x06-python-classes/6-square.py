#!/usr/bin/python3
"""Create a class Square"""


class Square:
    """A representation of a real world square.

    This Square object has only one attribute now

    Attribute:
        size: The length of the sides of the square.

    """

    def __init__(self, size=0, position=(0, 0)):
        """This __init__ method initializes the class with default
        value of 0 for the attribute size a default tuple 0f (0, 0)
        for the attribute position.

        Args:
            param1 (size): The size of the sides.

        """
        self.__size = size
        self.__position = position

    def area(self):
        """area: This method calculates and returns
        the area of the Square object
        """
        return (self.__size ** 2)

    def my_print(self):
        """my_print: Prints the Square object to stdout with
        # characters and position.
        It prints an empty line if size is 0.
        """
        if self.__size != 0:
            for i in range(0, self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print("", end="")
                for k in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
            return

    @property
    def size(self):
        """size: Is the length of the sides of the Square object.

        The attribute 'size' should always be an integer and must not
        be negative.
        """
        return (self.__size)

    @property
    def position(self):
        """Position: Is a tuple of 2 positive integers.

        The setter raises a TypeError exception indicating that
        position must be 2 positive integers.
        """
        return (self.__position)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
