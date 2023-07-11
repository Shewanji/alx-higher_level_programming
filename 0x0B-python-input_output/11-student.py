#!/usr/bin/python3
"""This module defines a class Student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with the provided
        first name, last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): List of attribute names to be retrieved.
            Defaults to None.

        Returns:
            dict: The dictionary representation of the Student instance.
        """
        if attrs is None:
            attrs = self.__dict__.keys()
        else:
            attrs = filter(lambda attr: attr in self.__dict__, attrs)

        student_dict = {attr: getattr(self, attr) for attr in attrs}
        return student_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance based on
        the provided JSON dictionary.

        Args:
            json (dict): JSON dictionary containing attribute names and values.

        Returns:
            None
        """
        for attr, value in json.items():
            setattr(self, attr, value)
