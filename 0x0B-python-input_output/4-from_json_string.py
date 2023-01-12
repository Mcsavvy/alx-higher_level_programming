#!/usr/bin/python3

"""
from_json_string(my_str) -> object:
    ...
"""


import json


def from_json_string(my_str):
    """
    this function creates a python object from a json repr

    Args:
        my_str: a json repr
    Returns:
        a python object
    """

    return json.loads(my_str)
