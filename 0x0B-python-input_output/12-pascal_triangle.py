#!/usr/bin/python3

"""
pascal_triangle(n) -> list[list[int]]
"""


def pascal_triangle(n: int) -> "list | list[list[int]]":
    """
    returns a list of lists of integers representing the pascal's
    triangle of n

    Args:
        n: an integer
    Returns: a list of lists representing the pascal triangle of n
    """

    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    tri = [[1]]

    for x in range(n - 1):
        tri.append([1] + [
            tri[x][y] + tri[x][y + 1] for y in range(x)
        ] + [1])
    return tri
