#!/usr/bin/python3
"""

Function that that prints My name is <first name> <last name>

"""


def say_my_name(first_name, last_name=""):
    """ Function that prints My name is <first name> <last name>

    Args:
        first_name: first name to evaluate
        last_name: last name to evaluate

    Returns:
        nothing.

    Raises:
        TypeError: if first name/last name are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}". format(first_name, last_name))
