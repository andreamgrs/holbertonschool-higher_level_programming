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


class Square(Rectangle):
    """Class for Square that inherits from BaseGeometry
    """
    def __init__(self, size):
        """Initializes square instance.

        Args:
            size(int): size of the square (private).
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Class method for get the area of a square.
        Returns:
            Area of square.
        """
        return super().area()
