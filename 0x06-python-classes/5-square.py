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

    @property
    def size(self):
        """ getter instance"""
        return self.__size

    @size.setter
    def size(self, value):
        """ instance to set the value of size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Public instance method
        returns the current square area
        """
        result = self.__size * self.__size
        return result

    def my_print(self):
        """ prints in stdout the square with the character # """
        if (self.__size) == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.size)
