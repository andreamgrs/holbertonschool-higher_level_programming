#!/usr/bin/python3
"""Module that appends a string at the end of a text file (UTF8)
    and returns the number of characters added
"""


def append_write(filename="", text=""):
    """Function that appends a string at the end of a text file
        and returns the number of characters added.

        Args:
            filename: filename
            text: text
    """
    with open(filename, "a", encoding="utf-8") as my_file:
        num_char = my_file.write(text)  #: write return num of characters
        return num_char
