#!/usr/bin/python3
"""Rectangle Class

    Raises:
        TypeError: if width not int
        ValueError: if width < 0
        TypeError: if height not int
        ValueError: if height < 0
"""


class Rectangle:
    """Class Defination
    """
    def __init__(self, width=0, height=0):
        """Rectangle Intialization
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return width value"""
        return(self.__width)

    @width.setter
    def width(self, value):
        """Set widht value"""
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return height value"""
        return(self.__height)

    @height.setter
    def height(self, value):
        """Set height value"""
        if (type(value) != int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value
