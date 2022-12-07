#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # create a new dictionary with key and value
    d = {key: value}
    # update the target dictionary
    a_dictionary.update(d)
    return a_dictionary
