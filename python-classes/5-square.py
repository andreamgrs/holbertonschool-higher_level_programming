#!/usr/bin/python3
"""Defines a Square class with a private size attribute."""


class Square:
    """Class for square

    Attributes:
        __size(int): The size of the square (private).
    """
    def __init__(self, size=0):
        """Initializes a Square instance.
        Args:
            size(int): size of the square.
        """
        self.size = size  #: call the setter

    @property
    def size(self):
        """Getter that returns the value of the private attribute __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter that assigns a new value to the private attribute __size.
        Args:
            value(int): size of the square.
        Raises:
                TypeError: if size is not an integer.
                ValueError: if size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Public method for get the area of a square.
        Returns:
            Area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """Public method that prints in stdout
        the square with the character # """
        if self.__size == 0:
            print("")
            return
        for num in range(self.__size):
            print("#" * self.__size)
