#!/usr/bin/python3
"""Module for read_file function
"""
def read_file(filename=""):
    """Function that reads from a file

        Args:
            filename: filename
    """
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read(), end="")
