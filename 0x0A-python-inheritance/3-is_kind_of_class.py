#!/usr/bin/python3
"""Function to check if the object is an instanse
    of class or inhertded from another class
"""


def is_kind_of_class(obj, a_class):
    """Function implementation"""

    if (isinstance(obj, a_class)):
        return True
    return False
