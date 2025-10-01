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

    def to_json(self, attrs=None):
        """ Public method that retrieves a dictionary representation
            of a Student instance.
            If attrs is a list of strings, only attribute names
            contained in this list must be retrieved.

            Otherwise, all attributes must be retrieved
        """
        data_dict = self.__dict__
        new_dict = {}
        if attrs is not None:
            for cont_data in data_dict:
                if cont_data in attrs:
                    new_dict[cont_data] = data_dict[cont_data]
            return new_dict
        else:
            return self.__dict__
