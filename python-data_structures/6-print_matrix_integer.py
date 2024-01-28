#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for arr in matrix:
        for el in arr:
            print("{:d}".format(el), end=" ")
        print("")
