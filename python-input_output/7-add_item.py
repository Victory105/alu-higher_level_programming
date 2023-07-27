#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file:"""


import sys
import os.path

from typing import List
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_items_to_list_and_save(args: List[str]):
    """
    Add all arguments to a Python list and save them to a file in JSON format.

    Args:
        args (List[str]): List of command-line arguments.
    """
    file_name = "add_item.json"

    # Check if the file exists and load its content if it does
    if os.path.exists(file_name):
        my_list = load_from_json_file(file_name)
    else:
        my_list = []

    # Add command-line arguments to the list
    my_list.extend(args)

    # Save the updated list to the file
    save_to_json_file(my_list, file_name)

if __name__ == "__main__":
    # Remove the first argument, which is the script name
    arguments = sys.argv[1:]
    add_items_to_list_and_save(arguments)
