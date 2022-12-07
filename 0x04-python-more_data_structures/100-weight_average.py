#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    weights = sum(map(lambda t: t[0] * t[1], my_list))
    div = sum(map(lambda t: t[1], my_list))
    return weights / div
