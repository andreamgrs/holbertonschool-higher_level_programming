#!/usr/bin/python3
""" Defines the function that returns True/False
    if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.
   """


def inherits_from(obj, a_class):
    """Function that returns True/False.
    Args:
            obj: instance of a class.
            a_class: class that inherited
            (directly or indirectly) from the specified class.
    Returns:
            True or False.
    """
    #: type(obj) devuelve True por que a = True
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
