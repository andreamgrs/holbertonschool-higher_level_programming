#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = list(map(lambda row: list(map(lambda num: num**2, row)), matrix))
    return square
