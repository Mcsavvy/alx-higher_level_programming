#!/usr/bin/python3
def new_in_list(my_list, idx, new_element):
    copy = my_list.copy()
    if idx >= 0 and idx < len(copy):
        copy[idx] = new_element
    return copy
