#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    final_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(my_pow(num))
        final_matrix.append(new_row)
    return final_matrix


def my_pow(num):
    return num ** 2
