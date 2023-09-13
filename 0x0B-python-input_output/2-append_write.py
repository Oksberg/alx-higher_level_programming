#!/usr/bin/python3
"""A function that appends a string. """


def append_write(filename="", text=""):
    """This function appends a string at the end of a text file.

    Args:
        filename (str): The file to append to.

    Return:
        The number of characters added.
        """

    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
