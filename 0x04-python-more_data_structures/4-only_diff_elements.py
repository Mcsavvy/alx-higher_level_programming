#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # get elements that are in exactly one set (symmetric_difference)
    elems = set_1.symmetric_difference(set_2)
    return elems
