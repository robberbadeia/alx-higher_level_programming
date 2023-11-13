#!/usr/bin/python3
"""Base Class"""
import json


class Base():
    """class implementation"""

    __nb_objects = 0

    def __init__(self, id=None):
        """class constractor : __init__ Function"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries): 
        """to json Function"""
        if list_dictionaries is None:
            return ("[]")
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """from json Function"""
        if json_string is None:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file Function"""
        lst = []
        if list_objs is not None:
            for item in list_objs:
                lst.append(cls.to_dictionary(item))
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            file.write(cls.to_json_string(lst))
