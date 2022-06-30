#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
        return
    
    for i in matrix:
        for elem in i:
            print("{:d} ".format(elem), end="")
        print()
