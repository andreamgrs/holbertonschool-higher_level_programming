#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    num_col = len(matrix[0])
    for row_cont in range(len(matrix)):
        for column_cont in range(num_col):
            if column_cont == num_col - 1:
                print("{:d}".format(matrix[row_cont][column_cont]), end="")
            else:
                print("{:d} ".format(matrix[row_cont][column_cont]), end="")
        print()
