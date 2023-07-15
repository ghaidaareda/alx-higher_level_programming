#!/usr/bin/python3
"""adds a new attribute to an object if it’s possible"""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if it's possible,
    otherwise raises a TypeError
    """
    if hasattr(obj, '__dict__'):
        obj.__setattr__(attribute, value)
    else:
        raise TypeError("can't add new attribute")
