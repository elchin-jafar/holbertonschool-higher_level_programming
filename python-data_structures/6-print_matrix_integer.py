#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for arr in matrix:
        if not isinstance(arr, list):
            print("{:d}".format(arr))
        else:
            for el in arr:
                print("{:d}".format(el), end=" ")
            print("")
