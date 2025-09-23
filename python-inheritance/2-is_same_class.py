#!/usr/bin/python3
""" Defines the function that returns True/False if the object is exactly
    an instance of the specified class.
   """


def is_same_class(obj, a_class):
    """Function that returns True/False if the object is exactly
    an instance of the specified class.
    Args:
            obj: instance of a class.
            a_class: the class to evaluate.
    Returns:
            True or False.
    """
    return type(obj) is a_class
