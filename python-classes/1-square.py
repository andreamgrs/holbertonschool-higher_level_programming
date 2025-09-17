#!/usr/bin/python3
"""Defines a Square class with a private size attribute."""


class Square:
    """Class for square

    Attributes:
        __size(int): The size of the square (private).
    """
    __size = 0

    def __init__(self, size):
        """Initializes a Square instance.

        Args:
            size(int): size of the square
        """
        self.__size = size
