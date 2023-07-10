#!/usr/bin/python3
"""Checks if object is an instance of a class
or an inherited class
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or
    if the object is an instance of a class
    that inherited from, the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is an instance of, or
              if the object is an instance of a class
              that inherited from, the specified class;
              False otherwise.
    """
    return isinstance(obj, a_class)
