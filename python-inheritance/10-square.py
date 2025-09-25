#!/usr/bin/python3
"""Module for BaseGeometry class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class for Square that inherits from BaseGeometry
    """
    def __init__(self, size):
        """Initializes square instance.

        Args:
            size(int): size of the square (private).
        """
        self.integer_validator("size", size)
        super().__init__(size, size)  #: call the constructor of Rectangle
        self.__size = size

    def area(self):
        """Class method for get the area of a square.
        Returns:
            Area of square.
        """
        return self.__size * self.__size
