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

    @staticmethod
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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string
        representation of list_objs to a file
        """
        filename = cls.__name__ + '.json'
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)
