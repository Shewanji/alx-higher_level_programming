#!/usr/bin/python3
"""This module MyList inherits from the list class"""


class MyList(list):
    """A class that inherits from list"""
    def print_sorted(self):
        """prints a sorted list"""
        sorted_list = sorted(self)
        print(sorted_list)
