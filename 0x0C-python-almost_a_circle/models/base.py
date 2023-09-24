#!/usr/bin/python3
"""Defines a class. """
import json


class Base:
    """The first class. """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes attribute id.

        Args:
            id (int): defaults to None
        """
        self.id = id

        if self.id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a JSON string representation of
        the list of dictionaries related to the class Base."""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
