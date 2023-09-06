#!/usr/bin/python3
"""Create a function to add 2 integers.
It takes 2 arguments and sums them.
a (int): The first parameter. Must be an integer.
b (int): The second parameter. Must be an integer. Defaults to 98.
"""


def add_integer(a, b=98):
    """Returns the sum of the 2 parameters.
    Raises TypeError: If param1 or param2 is not an integer.
    """

    if not isinstance(a, int):
        if isinstance(a, float):
            a = int(a)
        else:
            raise TypeError("a must be an integer")
    elif not isinstance(b, int):
        if isinstance(b, float):
            b = int(b)
        else:
            raise TypeError("b must be an integer")
    
    return a + b
