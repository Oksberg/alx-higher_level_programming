#!/usr/bin/python3
"""A function that uses JSON rep to write an object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """This function writes an object to a text file.

    Args:
        my_obj (str): The string to write.
    """

    with open(filename, "w") as file:
        json.dump(my_obj, file)
