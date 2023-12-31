#!/usr/bin/python3
"""
Creates a Base class that is the super for all the other classes.
"""
import json


class Base:
    """A class Base with private attribute and a constructor
    with one attribute.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes an attribute id with default value None.
        If no input id given for id, the private attribute is increm
        and assigned to id."""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON serialization of list_objs to a file.

        Args:
            list_objs (list): list of objects that inherits from Base.
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                list_of_dicts = [o.to_dictionary() for o in list_objs]
                json_file.write(Base.to_json_string(list_of_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns a list of JSON string representation.

        Returns:
            an empty list: if json_string is None or empty.
            a list: if json_string is not empty.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns a dictionary of all attributes.

        Args:
            **dictionary (dict): key/value pairs of attributes.
        """
        if dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(4, 7)
            else:
                new = cls(4)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances of the class."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as json_file:
                list_of_dicts = Base.from_json_string(json_file.read())
                return [cls.create(**dict) for dict in list_of_dicts]
        except FileNotFoundError:
            return []
