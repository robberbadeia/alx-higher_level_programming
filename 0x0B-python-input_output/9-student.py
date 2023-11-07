#!/usr/bin/python3
"""Class Student"""


class Student:
    """Class Implementation"""
    def __init__(self, first_name, last_name, age):
        """__init__ Implementation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return obj.__dic__"""
        return self.__dict__
