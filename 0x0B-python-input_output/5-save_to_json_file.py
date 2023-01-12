#!/usr/bin/python3

"""
this file contains a function that saves
the json representation of an object to
a file

"""

import json


def save_to_json_file(my_obj, filename):
    """
    writes the json representation of an object
    to a file. File is created if doesn't exist.

    Args:
        my_obj: a python object
        filename: the name/path of the file to write the json repr int
    """

    with open(filename, "w+") as f:
        json_string = json.dumps(my_obj)
        f.write(json_string)
