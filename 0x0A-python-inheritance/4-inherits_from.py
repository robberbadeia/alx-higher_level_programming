#!/usr/bin/python3
"""Function to check if the object is
    inhertded from another class
"""


def inherits_from(obj, a_class):
    """Function implementation"""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
