#!/usr/bin/python3
"""This module defines a file-writing function."""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8).

    Args:
        filename (str): The name of the file to be written.
        Defaults to an empty string.
        text (str): The string to be written to the file.

    Returns:
        None
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return len(text)
