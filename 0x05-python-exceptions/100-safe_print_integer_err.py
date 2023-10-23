#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    if (isinstance(value, int)):
        try:
            print("{:d}".format(value))
            return True
        except (TypeError, ValueError) as e:
            stderr.write("Exception: {}\n".format(e))
            return False
