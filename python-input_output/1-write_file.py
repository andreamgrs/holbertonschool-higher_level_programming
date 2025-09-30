#!/usr/bin/python3
"""Module that writes a string to a text file (UTF8)
    and returns the number of characters written
"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file
        and returns the number of characters written.

        Args:
            filename: filename
            text: text
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        num_char = my_file.write(text)  #: write return num of characters
        return num_char
