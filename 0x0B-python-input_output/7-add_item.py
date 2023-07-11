#!/usr/bin/python3
"""This module adds all arguments to a Python list and save them to a file."""


import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

# Read existing list from file if it exists
    try:
        existing_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_list = []

# Add arguments to the list
    arguments = sys.argv[1:]  # Exclude the script name from the arguments
    existing_list.extend(arguments)

# Save the updated list to file
    save_to_json_file(existing_list, "add_item.json")
