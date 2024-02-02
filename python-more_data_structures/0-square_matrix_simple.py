#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = list()
    for ls in matrix:
        new_ls = list(map(lambda x: x ** 2, ls))
        new_matrix.append(new_ls)
    return new_matrix
