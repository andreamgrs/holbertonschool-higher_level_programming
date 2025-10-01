#!/usr/bin/python3
""" Module that that defines a student by
    first name, last name and age.
"""


class Student:
    """ Class for Student.
    """
    def __init__(self, first_name, last_name, age):
        """ Instantiation with first_name, last_name and age.

            Public attributes:
                first_name (str): first name
                last_name (str): last name
                age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Public method that retrieves a dictionary representation
            of a Student instance.
        """
        return self.__dict__
