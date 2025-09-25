#!/usr/bin/python3
"""Module for BaseGeometry class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class for rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """Initializes a rectangle instance.

        Args:
            width(int): Width of the rectangle (private).
            height(int): Height of the rectangle (private).

        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Class method for get the area of a rectangle.
        Returns:
            Area of rectangle.
        """
        return self.__height * self.__width

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
