#!/usr/bin/python3
"""MYInt Class"""


class MyInt(int):
    """Class Implementation"""

    def __init__(self, num):
        """init implementation"""

        self.__num = num

    def __str__(self):
        """__str__ implementation"""

        return str(self.__num)

    def __eq__(self, value):
        """Override"""

        return self.real != value

    def __ne__(self, value):
        """Override"""

        return self.real == value
