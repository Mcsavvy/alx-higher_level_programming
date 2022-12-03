#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bools = []
    for i in my_list:
        bools.append(i % 2 == 0)
    return bools
