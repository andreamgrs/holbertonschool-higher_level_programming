#!/usr/bin/python3
""" Defines the function that returns True if the object is an instance
    of a class or of a class that inherited from, the specified class.
   """


def is_kind_of_class(obj, a_class):
    """Function that returns True/False.
    Args:
            obj: instance of a class.
            a_class: the class to evaluate.
    Returns:
            True or False.
    """
    return isinstance(obj, a_class)
