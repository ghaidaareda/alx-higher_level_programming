#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for  i in map(square_matrix_simple, matrix=[]):
        print(i * i)
