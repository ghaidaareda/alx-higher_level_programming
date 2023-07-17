#!/usr/bin/python3
""" class Base """


import json


class Base:
    """
    class Base
    “base” of all other classes in this project
     to manage id attribute in all future classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        returns the JSON string
        representation of list_dictionaries
        """
        if list_dictionaries is not None:
            json_dic = json.dumps(list_dictionaries)
            return json_dic
        else:
            return "[]"
