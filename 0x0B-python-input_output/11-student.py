#!/usr/bin/python3
"""Class Student"""


class Student:
    """Class Implementation"""
    def __init__(self, first_name, last_name, age):
        """__init__ Implementation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return obj.__dic__"""
        if attrs is None:
            return self.__dict__
        else:
            dic = {}
            for attr in attrs:
                if attr in self.__dict__.keys():
                    dic[attr] = self.__dict__[attr]
            return dic

    def reload_from_json(self, json):
        """Return:Transfer all attributes of json to self"""
        for k, v in json.items():
            setattr(self, k, v)
