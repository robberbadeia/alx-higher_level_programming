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

    def area(self):
        """implement rectangle area"""

        return self.__height * self.__width

    def __str__(self):
        """Implement str() and print() value"""

        return("[Rectangle] {}/{}".format(self.__width, self.__height))
