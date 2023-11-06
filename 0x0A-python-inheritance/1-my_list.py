#!/usr/bin/python3
"""Class inherite the list class"""


class MyList(list):
    """class Myclass"""

    def print_sorted(self):
        """Method to sort a list"""

        print(sorted(self))
