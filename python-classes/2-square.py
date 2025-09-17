#!/usr/bin/python3
"""Defines a Square class with a private size attribute."""


class Square:
    """Class for square

    Attributes:
        __size(int): The size of the square (private).
    """
    __size = 0

    def __init__(self, size=0):
        """Initializes a Square instance.

        Args:
            size(int): size of the square
        """
        self.__size = size

        """Raises:
                TypeError: if size is not an integer.
                ValueError: if size is less than 0
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")