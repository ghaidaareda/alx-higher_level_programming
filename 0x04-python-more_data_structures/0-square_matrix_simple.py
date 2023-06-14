#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list (map(lambda raw: list(map(lambda col:col *col, raw)), matrix))
