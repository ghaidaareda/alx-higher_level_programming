#!/usr/bin/python3
"""
function that returns True if the object is an instance of a
subclass of specefied class, otherwise false
"""


def inherits_from(obj, a_class):
    """
    check if obj is instance of a sub class of class (a_class)
    """
    return isinstance(obj, a_class)
