#!/usr/bin/python3


"""
This file contains a function the divides all elements in a matrix
matrix_divided:
    divides all elements in a matrix
"""


def matrix_divided(matrix, div):
    """
    divides all elements in a matrix
    """
    flag = False
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        flag = True
    else:
        for row in matrix:
            if not isinstance(row, list):
                flag = True
                break
            for n in row:
                if not isinstance(n, (float, int)):
                    flag = True
                    break
    if flag:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    length = len(matrix[0])
    if not all(map(lambda row: len(row) == length, matrix[1:])):
        raise TypeError("Each row of the matrix must have the same size")
    return [[float("{:.2f}".format(n / div)) for n in row] for row in matrix]
