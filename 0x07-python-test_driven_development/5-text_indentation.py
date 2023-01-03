#!/usr/bin/python3


"""
This file contains a function text_indentation(text)
that prints a text with 2 new lines after each of these
characters (., ?, :)
"""


def text_indentation(text):
    """
    this function prints a text with 2 new lines after each of
    these characters (., ?, :)
    """
    flag = False
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i, c in enumerate(text):
        if c != ' ':
            flag = True
        if c in ".:?":
            print("{}\n".format(c))
            flag = False
        elif flag:
            print(c, end="")
    print()
