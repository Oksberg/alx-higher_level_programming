#!/usr/bin/python3
"""A function to check instance """


def is_same_class(obj, a_class):
    """This function checks if a given object is an instance of
    the class specified.
    It returns True if it's an instance and False if it's not.
    """

    return isinstance(obj, a_class) and type(obj) == a_class
