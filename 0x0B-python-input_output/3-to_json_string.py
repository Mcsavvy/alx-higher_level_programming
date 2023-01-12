#!/usr/bin/python3

"""
this file contains a function that returns
the json representation of an object
"""


import json


def to_json_string(my_object):
    """
    returns a json representation of an object

    Args:
        my_object: a python object
    Returns:
        a string which is the json representation of my_object
    """
    json_string = json.dumps(my_object)
    return json_string
