#!/usr/bin/python3
""" class Square that defines a square """


class Square:
    """ class represtents a square """
    def __init__(self, size=0):
        """
        init function defines a square
        size : Private instance attribute
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
