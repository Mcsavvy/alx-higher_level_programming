#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # create a new empty dict
    d = {}
    # iterate through every key in the supplied dict
    for key in a_dictionary:
        # add the key to the new dict and set the vale to be 2x the initial
        d[key] = 2 * a_dictionary[key]
    return d
