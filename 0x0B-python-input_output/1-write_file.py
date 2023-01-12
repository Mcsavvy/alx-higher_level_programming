#!/usr/bin/python3

"""
this file contains a function `write_file` that writes
a content into a file
"""


def write_file(filename="", text=""):
    """
    writes content to a file. Creates file it doesn't exists.

    Args:
        filename: the name/path of the file to write into
        text: content to write into the file
    """

    with open(filename, 'w+') as f:
        written = f.write(text)
    return written
