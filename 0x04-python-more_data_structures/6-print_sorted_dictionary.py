#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # get all keys of the dictionary
    keys = a_dictionary.keys()

    # iterate through the keys sorted in ascending order
    for key in sorted(keys):
        print("{}: {}".format(key, a_dictionary[key]))
