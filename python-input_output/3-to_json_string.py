#!/usr/bin/python3
"""Module that returns the JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """Function that returns the JSON representation of an object (string).

        Args:
            my_obj: object like a list, dic etc..
    """
    json_str = json.dumps(my_obj)
    return json_str
