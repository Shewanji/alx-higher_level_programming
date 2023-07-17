#!usr/bin/python3

import os
import csv
import json


class Base:
    """
    Base class for managing ID attribute in all future classes.

    Attributes:
        __nb_objects (int): Private class attribute to keep track
        of the number of objects created.
        id (int): Public instance attribute representing the ID of an object.

    Methods:
        __init__(self, id=None): Class constructor to initialize the instance.
            If 'id' is provided, assigns the provided ID
            to the instance's 'id' attribute.
            If 'id' is not provided, increments the '__nb_objects' counter
            and assigns the new value to the instance's 'id' attribute.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with all attributes already set.

        Args:
            **dictionary (dict): Dictionary of attribute names and values.

        Returns:
            Base: Instance with attributes set from the dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            dummy_instance = None

        if dummy_instance is not None:
            dummy_instance.update(**dictionary)

        return dummy_instance

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list represented by the JSON string.

        Args:
            json_string (str): JSON string representation of a list.

        Returns:
            list: List represented by the JSON string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances from a file.

        Returns:
            list: List of instances.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                instances = [
                    cls.create(**dictionary) for dictionary in dictionaries
                ]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): List of instances.

        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string(
            [obj.to_dictionary() for obj in list_objs]
        ) if list_objs else "[]"
        with open(filename, 'w') as file:
            file.write(json_string)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes instances to CSV file."""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([
                        obj.id,
                        obj.width,
                        obj.height,
                        obj.x,
                        obj.y
                    ])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes instances from CSV file."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        dictionary = {
                            "id": int(row[0]),
                            "width": int(row[1]),
                            "height": int(row[2]),
                            "x": int(row[3]),
                            "y": int(row[4]),
                        }
                    elif cls.__name__ == "Square":
                        dictionary = {
                            "id": int(row[0]),
                            "size": int(row[1]),
                            "x": int(row[2]),
                            "y": int(row[3]),
                        }
                    instance = cls.create(**dictionary)
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []
