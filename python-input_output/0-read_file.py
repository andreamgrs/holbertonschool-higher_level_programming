#!/usr/bin/python3
"""Module for read_file function
"""
def read_file(filename=""):
    """Public function to read a text file UTF8 
        """
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read())
