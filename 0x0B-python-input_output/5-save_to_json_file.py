#!/usr/bin/python3
"""This module defines a JSON file-writing function"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The object to be written.
        filename (str): The name of the file to save the JSON representation.

    Returns:
        None
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
