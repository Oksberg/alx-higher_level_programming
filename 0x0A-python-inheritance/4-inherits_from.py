#!/usr/bin/python3
"""Function to check subclass"""


def inherits_from(obj, a_class):
    """This function checks if the object obj is an subclass of
    a_class, but for that to be true, obj must not be an instance
    of a_class so it checks it's not before checking subclass.
    """

    return issubclass(type(obj), a_class) and type(obj) != a_class
