#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # check if key is in the dict
    if key in a_dictionary:
        # delete the key
        del a_dictionary[key]
    return a_dictionary
