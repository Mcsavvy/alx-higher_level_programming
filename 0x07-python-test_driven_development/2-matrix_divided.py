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
    if is not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not matrix:
        return []
    if not isinstance(matrix, list):
        flag = True
    elif not all(map(lambda row: isinstance(row, list) and all(
        map(lambda n: isinstance(n, (int, float)), )), matrix)):
        flag = True
    if flag:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    l = len(matrix[0])
    if not all(map(lambda row: len(row) == l, matrix)):
        raise TypeError("Each row of the matrix must have the same size")
    return [["{:.2f}".format(n / div) for n in row] for row in matrix]
