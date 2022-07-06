#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    a = matrix[0]
    b = matrix[1]
    return list(map(lambda x: x*x, a, b))
