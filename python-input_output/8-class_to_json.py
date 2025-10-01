#!/usr/bin/python3
""" Module that returns the dictionary description
    with simple data structure (list, dictionary,
    string, integer and boolean) for JSON serialization of an object.
"""
import json


def class_to_json(obj):
    """ Function that returns the dictionary description
        with simple data structure for JSON serialization of an object.

        Args:
            obj: is an instance of a Class.
    """
    data = obj.__dict__
    json_serialization = json.dumps(data)

    return json_serialization
