#!/usr/bin/python3
""" add function and its doctest"""


def add_integer(a, b=98):
    """
    function to add integers
    consider float as integer
    a,b are arguments
    if b not exist it is 98 by default
    """
    try:
        if isinstance(a, float):
            a = int(a)
        elif not isinstance(a, int) and not isinstance(a, float):
            raise TypeError("a must be an integer")
        elif a is None:
            raise TypeError("add_integer() missing 1 required positional argument: 'a'")
        elif isinstance(b, float):
            b = int(b)
        elif not isinstance(b, int) and not isinstance(b, float):
            raise TypeError("b must be an integer")
        return int(a + b)
    except TypeError as e:
        raise TypeError(str(e))
