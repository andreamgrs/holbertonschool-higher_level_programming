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
