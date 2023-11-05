#!/usr/bin/python3
"""Geometry module"""


class BaseGeometry:
    """Class Implementation"""

    def area(self):
        """Function Implementation"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function Implementation"""

        if (type(value) != int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0")
