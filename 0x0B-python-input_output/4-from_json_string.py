#!/usr/bin/python3
"""A function that returns an object rep by JSON string"""
import json


def from_json_string(my_str):
    """This function returns  an object represented by a JSON string.

    Args:
        my_str (str): The string to evaluate.

    Return:
        An object represented by JSON string
    """

    return json.loads(my_str)
