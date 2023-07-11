#!/usr/bin/python3
"""This module defines a text file-reading function"""


def read_file(filename=""):
    """
    Reads a text file and prints its contents to stdout.

    Args:
        filename (str): The name of the file to be read.
        Defaults to an empty string.

    Returns:
        None
    """
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
