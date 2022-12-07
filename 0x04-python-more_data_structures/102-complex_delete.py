#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not isinstance(a_dictionary, dict):
        return None
    for key, val in tuple(a_dictionary.items()):
        if val == value:
            del a_dictionary[key]
    return a_dictionary
