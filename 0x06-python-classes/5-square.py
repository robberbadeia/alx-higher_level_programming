#!/usr/bin/python3
"""_Class Square_"""


class Square:
    """init method
    """
    def __init__(self, size=0):
        self.size = size
        """_size method_

        Raises:
            TypeError: _description_
            ValueError: _description_
        """
    @property
    def size(self):
        return (self.__size)
        """_size.setter_

        Raises:
            TypeError: _description_
            ValueError: _description_

        Returns:
            _type_: _description_
        """
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
            _type_: _description_
        """
        return (self.__size ** 2)

    def my_print(self):
        """_summary_
        """
        if (self.__size == 0):
            print("")
        else:
            for x in range(self.__size):
                for y in range(self.__size):
                    print("#", end='')
                print("")
