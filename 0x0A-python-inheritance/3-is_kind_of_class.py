#!/usr/bin/python3
"""A function to check tpye and or subclass """


def is_kind_of_class(obj, a_class):
    """This functions checks if anobject is an instance of the
    class specified or if it is a subclass of the specified class.
    """

    return issubclass(type(obj), a_class)
