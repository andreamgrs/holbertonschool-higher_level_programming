#!/usr/bin/python3
"""
    Returns a sum of 2 numbers
"""


def add_integer(a, b=98):
    """ Function that adds two int or float numbers.
    Args:
        a: first number.
        b: second number.
    Returns:
        The addition of both numbers
    Raises:
        TypeError if a or b ar not intergers or float numbers.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if a == float('inf') or a == -float('inf'):
        raise TypeError("a must be an integer")
    if b == float('inf') or b == -float('inf'):
        raise TypeError("b must be an integer")
    if type(a) or type(b) is [float]:
        a = int(a)
        b = int(b)
    return a + b
