#!/usr/bin/python3
""" Module that writes an Object to a text file,
    using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """ Function that writes an Object to a text file,
        using a JSON representation.

        Args:
            my_obj: object like a list, dic etc..
            filename: filename
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        json.dump(my_obj, my_file)
