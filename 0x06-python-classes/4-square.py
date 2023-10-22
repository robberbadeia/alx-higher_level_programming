#!/usr/bin/python3
"""Dfine a Square Class"""


class Square:
    """_summary_
    """
    def __init__(self, size=0):
        """__init method

        Args:
            size (int)
        """
        self.size = size

    @property
    def size(self):
        """_summary_

        Returns:
            _type_: _description_
        """

        return (self.__size)

    @size.setter
    def size(self, value):
        """_summary_

        Args:
            value (_type_): _description_

        Raises:
            TypeError: _description_
            ValueError: _description_

        """
        if (type(value) != int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """_summary_

        Returns:
            Area of Square
        """
        return (self.__size ** 2)
