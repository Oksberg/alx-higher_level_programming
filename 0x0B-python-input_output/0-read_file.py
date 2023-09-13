#!/usr/bin/python3
"""Creates a function for reading a file."""


def read_file(filename=""):
    """This function reads a text file and prints it to stdout.
    It uses the with statement.
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
