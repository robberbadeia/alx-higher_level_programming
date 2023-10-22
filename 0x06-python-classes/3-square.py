#!/usr/bin/python3
"""Dfine a Square Class"""


class Square:
    """_summary_
    """
    def __init__(self, size=0):
        """_init_

        Args:
            size (int): The size of Square

        Raises:
            TypeError: _description_
            ValueError: _description_
        """
        if (type(size) != int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self._Square__size = size

    def area(self):
        """Return the area of the Square
        """
        return (self._Square__size ** 2)
