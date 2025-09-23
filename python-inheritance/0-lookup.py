#!/usr/bin/python3
""" Defines the function lookup that returns the list of
    available attributes and methods of an object.
    """


def lookup(obj):
    """Function that returns the list of available attributes
    and methods of an object.
    Args:
            obj: instance of a class
    Returns:
            List of available attributes and methods of an object.
    """
    return dir(obj)
