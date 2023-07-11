#!/usr/bin/python3
"""This module defines a JSON-to-object function"""
import json


def from_json_string(my_str):
    """
    Returns the Python data structure represented by a JSON string.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    python_object = json.loads(my_str)
    return python_object
