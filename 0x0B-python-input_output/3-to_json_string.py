#!/usr/bin/python3
"""
function that returns the JSON representation of an object (string)
"""


def to_json_string(my_obj):
    """ JSON representation """
    import json

    my_obj_json = json.dumps(my_obj)
    return my_obj_json
