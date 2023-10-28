#!/usr/bin/python3
"""_add_integar_Function to add two int or float numbers
"""


def add_integer(a, b=98):
    sum = 0
    if (type(a) != int and type(a) != float):
        raise TypeError("a must be an integer")
    if (type(b) != int and type(b) != float):
        raise TypeError("b must be an integer")
    sum = int(a) + int(b)
    return (sum)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")