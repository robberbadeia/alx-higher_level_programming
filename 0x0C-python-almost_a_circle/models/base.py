#!/usr/bin/python3
"""Base Class"""


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
