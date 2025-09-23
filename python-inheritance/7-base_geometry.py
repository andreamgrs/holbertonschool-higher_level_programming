#!/usr/bin/python3
"""Module for BaseGeometry class
"""


class BaseGeometry:
    """Class for BaseGeometry
    """

    def area(self):
        """Public instance method that raises
            an Exception with the message area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates value.

        Args:
            name(string): name as first parameter
            value(int): second parameter

        Raises:
                TypeError: if value is not ant integer.
                ValueError: if value is less or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
