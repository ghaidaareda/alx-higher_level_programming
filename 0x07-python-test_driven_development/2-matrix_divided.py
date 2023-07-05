#!/usr/bin/python3
""" matrix_divided function"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix

    Arguments:

    matrix: must be a list of lists ints or floats
    with rows of the same size

    div: must be a number int or float and not 0
    """
    new_matrix = []
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    elif not isinstance(matrix, list):
        raise TypeError(msg)
    else:
        len_first_sublist = len(matrix[0])
        if not all(len(sublist) == len_first_sublist for sublist in matrix):
            raise TypeError("Each row of the matrix must have the same size")
        for sublist in matrix:
            raw = []
            for i in sublist:
                if not isinstance(sublist, list):
                    raise TypeError(msg)
                elif not isinstance(i, int) and not isinstance(i, float):
                    raise TypeError(msg)
                result = round(float(i / div), 2)
                raw.append(result)
            new_matrix.append(raw)
        return new_matrix
