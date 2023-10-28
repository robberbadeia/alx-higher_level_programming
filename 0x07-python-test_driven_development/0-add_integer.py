#!/usr/bin/python3
"""_add_integar_Function to add two int or float numbers
"""


def add_integer(a, b=98):
    """_summary_

    Args:
        a (_type_): _description_
        b (int, optional): _description_. Defaults to 98.

    Raises:
        TypeError: _description_
        TypeError: _description_

    Returns:
        _type_: _description_
    """
    sum = 0
    if (type(a) != int and type(a) != float):
        raise TypeError("a must be an integer")
    if (type(b) != int and type(b) != float):
        raise TypeError("b must be an integer")
    sum = int(a) + int(b)
    return (sum)
