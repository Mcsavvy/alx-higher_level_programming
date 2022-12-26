#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    index = 0
    while index < x:
        try:
            e = my_list[index]
        except IndexError:
            break
        print("{}".format(e), end="")
        index += 1
    print("")
    return index
