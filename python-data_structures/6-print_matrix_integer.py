#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for cont, value in enumerate(row):
            if cont == len(row)-1:
                print("{:d}".format(value))
            else:
                print("{:d} ".format(value), end="")
            cont = cont +1
    print()
