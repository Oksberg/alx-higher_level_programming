#!/usr/bin/python3
"""This function makes a Python class-to-JSON."""


def class_to_json(obj):
    """This function returns the dictionary representation of a
    simple data structure."""

    return obj.__dict__
