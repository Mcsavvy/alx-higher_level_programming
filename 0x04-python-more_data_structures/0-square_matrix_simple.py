#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    squared_matrix = [
            [0 for j in range(len(matrix[0]))]
            for i in range(len(matrix))]

    # Iterate over the elements of the input matrix and compute the square
    # of each value.
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            squared_matrix[i][j] = matrix[i][j] * matrix[i][j]

    # Return the new matrix
    return squared_matrix
