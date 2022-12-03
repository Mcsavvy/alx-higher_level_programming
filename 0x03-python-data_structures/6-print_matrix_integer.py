#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        for i, c in enumerate(r):
            s = ' '
            if i == len(r) - 1:
                s = ''
            print("{:d}".format(c, s), end=s)
        print("")
