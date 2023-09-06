#!/usr/bin/python3
"""Create a function to add 2 integers"""


def add_integer(a, b=98):
    """This is a fuction that adds 2 integers.
    
    Args:
        a (int): The first parameter. Must be an integer.
        b (int): The second parameter. Must be an integer. Defaults to 98.

    Returns:
        int: Returns the sum of param1 and param2.

    Raises:
        TypeError: If param1 or param2 is not an integer.
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
