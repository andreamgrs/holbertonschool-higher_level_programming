#!/usr/bin/python3
"""Module for Mylist class
"""


class MyList(list):
    """Class MyList that inherits from list
    """
    def print_sorted(self):
        """Public instance method that prints the list, but sorted."""
        print(sorted(self))
