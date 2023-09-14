#!/usr/bin/python3
"""Defines a class MyList"""


class MyList(list):
    """This class MyList inherits from the built-in list."""

    def print_sorted(self):
        """This function returns a list sorted in ascending order."""
    
        return self.sort()
