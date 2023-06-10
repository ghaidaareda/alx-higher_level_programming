#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for raw in matrix:
        for col in raw:
            print("{:d}".format(col), end=" " if col != raw [- 1] else "")
        print()
