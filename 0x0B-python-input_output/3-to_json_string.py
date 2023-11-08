#!/usr/bin/python3
"""A function that returns JSON representation"""
import json


def to_json_string(my_obj):
    """This function return JSON representation.

    Args:
        my_obj (str): The object to evaluate.

    Return:
        JSON representation.
        """

    return json.dumps(my_obj)
