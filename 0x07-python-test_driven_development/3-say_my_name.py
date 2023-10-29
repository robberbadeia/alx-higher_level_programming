#!/usr/bin/python3
"""_Function to say hello_
"""


def say_my_name(first_name, last_name=""):
    """_summary_

    Args:
        first_name (_type_): _description_
        last_name (str, optional): _description_. Defaults to "".

    Raises:
        TypeError: _description_
        TypeError: _description_
    """
    if (type(first_name) != str):
        raise TypeError("first_name must be a string")
    if (type(last_name) != str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
