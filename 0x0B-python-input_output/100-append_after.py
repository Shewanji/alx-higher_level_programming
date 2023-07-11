#!/usr/bin/python3
"""This module defines a text file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text into a file after each line
    containing a specific string.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in each line.
        new_string (str): The line of text to insert after lines
        containing the search string.

    Returns:
        None
    """
    with open(filename, "r") as file:
        lines = file.readlines()

    with open(filename, "w") as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + "\n")
