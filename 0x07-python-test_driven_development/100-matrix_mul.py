#!/usr/bin/python3


"""
This file contains a function that multiplies two matrices
matrix_mul:
    multiplies a matrix
"""


def matrix_mul(m_a, m_b):
    """
    multiplies two matrices
    returns a new matrix which is product of the multiplication
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isintance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isintance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not m_a or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if not m_b or m_b == [[]]:
        raise ValueError("m_b can't be empty")
