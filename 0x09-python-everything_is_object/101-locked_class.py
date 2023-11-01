#!/usr/bin/python3
"""Defines a class."""


class LockedClass:
    """
    LockedClass has no attributes but restrict the naming of
    any new attribute to "first_name".
    """
    __slots__ = "first_name"
