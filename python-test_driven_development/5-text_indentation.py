#!/usr/bin/python3
"""

Function that prints a text with 2 new lines
after each of these characters: ., ? and :

"""


def text_indentation(text):
    """ Function prints a text with 2 new lines
    after each of these characters: ., ? and :

    Args:
        text: text to evaluate

    Returns:
        The text with 2 new lines after each characters

    Raises:
        TypeError: if text is not a string
    """
    new_text = text.replace(".", ".\n\n").replace("?", "?\n\n").replace(":", ":\n\n")
    print(new_text)
