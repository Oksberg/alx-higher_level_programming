#!/usr/bin/python3
"""A search and add function"""


def append_after(filename="", search_string="", new_string=""):
    """This function search for a specified string and insert another
    string after it.

    Args:
        filename (file): The file to evaluate.
        search_string (str): The string to search for.
        new_string (str): The string to insert.
    """

    file_content = ""
    with open(filename, "r") as file:
        for line in file:
            file_content += line
            if search_string in line:
                file_content += new_string
    with open(filename, "w") as file:
        file.write(file_content)
