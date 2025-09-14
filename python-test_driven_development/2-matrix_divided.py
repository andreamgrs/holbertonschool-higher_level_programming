#!/usr/bin/python3
"""

This module is composed by a function that divides the numbers of a matrix

"""


def matrix_divided(matrix, div):
    """ Function that divides the integer/float numbers of a matrix

    Args:
        matrix: list of a lists of integers/floats
        div: number which divides the matrix

    Returns:
        A new matrix with the result of the division

    Raises:
        TypeError: If matrix is not a list of lists of int or floats
                   If div is not an int or float number
                   If the lists of the matrix don't have the same size

        ZeroDivisionError: If div is zero
    """
    if not matrix or not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) not in [float, int] or div == float('inf') or div == -float('inf'):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    len_matrix = 0
    for cont in matrix:
        if len_matrix != 0 and len(cont) != len_matrix:
            raise TypeError("Each row of the matrix must have the same size")
        for num in cont:
            if not isinstance(num, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        len_matrix = len(cont)
    new_matrix = list(map(lambda x: list(map(lambda y: round(y/div, 2), x)), matrix))
    return new_matrix
