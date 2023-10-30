#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:
    """Representation"""

    def __init__(self, width=0, height=0):
        """Initialization

        Args:
            width (int):The width of the new rectangle.
            height (int):The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get Width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate rectangler area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Claculate Rectangler preimeter"""
        if (self.__height == 0):
            return (0)
        if (self.__height == 0):
            return (0)
        return (2*(self.__height + self.__width))

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        pic = []
        for i in range(self.__height):
            [pic.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                pic.append('\n')
        return ("".join(pic))

    def __repr__(self):
        """prints a rectangle using '#'"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """prints a rectangle using '#'"""
        print("Bye rectangle...")
