#!/usr/bin/python3
"""Geometry module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Implementation"""

    def __init__(self, width, height):
        """init Function"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
