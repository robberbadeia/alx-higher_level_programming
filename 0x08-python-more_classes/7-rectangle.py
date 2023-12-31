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

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Rectangle Intialization
        """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

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

    def area(self):
        """Calculate rectangler area"""
        return(self.__height * self.__width)

    def perimeter(self):
        """Claculate Rectangler preimeter"""
        if (self.__height == 0 or self.__width == 0):
            return 0
        return (2 * (self.__height + self.__width))

    def __str__(self):
        """prints a rectangle using '#'"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        pic = []
        for row in range(self.__height):
            for ele in range(self.__width):
                pic.append(str(self.print_symbol))
            if (row != self.__height - 1):
                pic.append("\n")
        return("".join(pic))

    def __repr__(self):
        """prints a rectangle using '#'"""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
