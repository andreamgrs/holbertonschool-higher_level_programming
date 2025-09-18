#!/usr/bin/python3
"""Defines a Square class with a private size attribute."""


class Square:
    """Class for square

    Attributes:
        __size(int): The size of the square (private).
        __position(int): Coordinates of a square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a Square instance.
        Args:
            size(int): size of the square.
        """
        self.size = size  #: call setter size
        self.position = position  #: call setter position

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

    @property
    def position(self):
        """Getter that returns the value of the private attribute __position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter that assigns a new value to the private attribute __size.
        Args:
            value(int): coordinates of the square.
        Raises:
                TypeError: if position is not a tuple of 2 + int.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")

        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        for num in range(self.__position[1]):
            print("")

        for num in range(self.__size):
            if self.__position[0] == 1:
                print(" " * self.__position[0] + "#" * self.__size)
            else:
                print("-" * self.__position[0] + "#" * self.__size)
