#!/usr/bin/python3

"""
the file contains a function `load_from_json_file`
that constructs a python object from a json repr read from a file.
"""


import json


def load_from_json_file(filename):
    """
    creates an object from a json repr read from a file

    Args:
        filename: the name/path of the file to read json repr from
    Returns:
        a python object
    """

    with open(filename, 'r') as f:
        json_string = f.read()
    my_object = json.loads(json_string)
    return my_object
