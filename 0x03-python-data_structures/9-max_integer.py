#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    m = my_list[0]
    for i in my_list[1:]:
        if i > m:
            m = i
    return m
