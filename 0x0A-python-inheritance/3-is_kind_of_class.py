#!/usr/bin/python3
"""
function that returns True if the object is an instance of a class
or of inherited class, otherwise false
"""


def is_kind_of_class(obj, a_class):
    """
    check if obj is instance of a_class
    or of a subdivision
    """
    return isinstance(obj, a_class)
