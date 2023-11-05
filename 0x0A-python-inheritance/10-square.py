#!/usr/bin/python3
"""Class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class implementation"""

    def __init__(self, size):
        """init Function"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
