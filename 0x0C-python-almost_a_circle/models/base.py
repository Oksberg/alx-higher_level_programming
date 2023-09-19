#!/usr/bin/python3
"""Defines a class. """


class Base:
    """The first class. """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes attribute id.

        Args:
            id (int): defaults to None
        """
        self.id = id

        if self.id == None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
