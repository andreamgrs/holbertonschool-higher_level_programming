#!/usr/bin/python3
"""Module for a rectangle class
"""


class Rectangle:
    """Class for rectangle

    Attributes:
        __width(int): Width of the rectangle (private).
        __height(int): Height of the rectangle (private).
    """
    def __init__(self, width=0, height=0):
        """Initializes a rectangle instance.

        Args:
            width(int): Width of the rectangle
            height(int): Height of the rectangle

        """
        self.width = width  #: call the setter
        self.height = height

    @property
    def width(self):
        """Getter that returns the value of the private attribute __width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter that assigns a new value to the private attribute __width.

        Args:
            value(int): width of the rectangle.
        Raises:
                TypeError: if width is not an integer.
                ValueError: if width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter that returns the value of the private attribute __height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter that assigns a new value to the private attribute __height.

        Args:
            value(int): height of the rectangle.
        Raises:
                TypeError: if height is not an integer.
                ValueError: if height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Class method for get the area of a rectangle.
        Returns:
            Area of rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """Class method for get the perimeter of a rectangle.
        Returns:
            perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Method that prints the rectangle with the character # """
        str_rec = []
        if self.__width == 0 or self.__height == 0:
            print("")
            return
        for num in range(self.__height):
            str_rec.append("#" * self.__width)
        return "\n".join(str_rec)

    def __repr__(self):
        """Method that return a string representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"
