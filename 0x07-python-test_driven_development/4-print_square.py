#!/usr/bin/python3
"""Function to print # Square
"""


def print_square(size):
    """
    function to print square
    """
    if (type(size) != int):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    if (type(size) == float and size < 0):
        raise TypeError("size must be an integer")
    for row in range(size):
        for col in range(size):
            print("#", end="")
        print("")
