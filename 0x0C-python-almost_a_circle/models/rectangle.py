#!/usr/bin/python3
"""Class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class Implementation"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__ Class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width
    @property
    def height(self):
        """height getter"""
        return self.__height
    @property
    def x(self):
        """x getter"""
        return self.__x
    @property
    def y(self):
        """y getter"""
        return self.__y

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
        
    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return area calculation"""
        return self.width * self.height

    def display(self):
        """Return display which represent widht, height"""
        if self.y > 0:
            for i in range(self.y):
                print()
        for row in range(self.__height):
            if self.x > 0:
                for i in range(self.x):
                    print(" ", end="")
            for col in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        """Retur setring"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if len(args) == 1:
            self.id = args[0]
        elif len(args) == 2:
            self.id = args[0]
            self.width = args[1]
        elif len(args) == 3:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
        elif len(args) == 4:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
        elif len(args) == 5:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        elif len(args) == 0:
            for (k, v) in kwargs.items():
                if k == "id":
                    self.id = v
                if k == "width":
                    self.width = v
                if k == "height":
                    self.height = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v
    def to_dictionary(self):
        """to dict function"""
        return {"x": self.x, "y": self.y, "id": self.id, "height": self.height, "width": self.width}