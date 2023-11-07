#!/usr/bin/python3
"""Create an empty class """


class BaseGeometry:
    """This class has no attribute or method defined.
    It is an empty class.
    """

    def area(self):
        """This is method to calculate the area of the object.
        It has not been implemented yet so an exception is raised.
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This method validates the value of the identifier "name".
        It raises a TypeError if the value is not an integer,
        and a ValueError if it is not positive. The identifier "name" must be a string.
        """

        if not isinstance(name, str):
            raise TypeError("identifier must be a string")

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
