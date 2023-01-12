#!/usr/bin/python3

"""
this file contains a function `append_write` that adds
a text to a given file
"""


def append_write(filename="", text=""):
    """
    appends new text to a file. creates the file if it doesn't  exist.

    Args:
        filename: the name/path of the file to write into
        text: the text to be appended into the file
    Returns:
        the number of characters written into the file
    """

    with open(filename, 'ab+') as f:
        return f.write(text.encode("utf-8"))
