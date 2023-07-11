#!/usr/bin/python3
"""This module defines a JSON file-reading function"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        object: The object created from the JSON file.
    """
    with open(filename, "r") as file:
        json_data = json.load(file)
        return json_data
