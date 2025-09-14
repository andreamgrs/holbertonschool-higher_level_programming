#!/usr/bin/python3
"""

Function that that prints a square with the character #.

"""


def print_square(size):
    """ Function that prints a square with the character #.

    Args:
        size: is the size length of the square

    Returns:
        nothing.

    Raises:
        TypeError: if size is not and int
        TypeError: if size is float and less than 0
        ValueError: if size is less than 0
    """
    if type(size) not in [int]:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    len_row = size
    for row in range(len_row):
        for column in range(len_row):
            print("#", end="")
        print()
