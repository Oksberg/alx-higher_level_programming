#!/usr/bin/python3
"""Defines a function that writes string to a text file."""



def write_file(filename="", text=""):
    """This function writes a string to a text file.

    Args:
        filename (str): Name of the file to write to.

    Returns:
        The number of characters written.
    """

    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
