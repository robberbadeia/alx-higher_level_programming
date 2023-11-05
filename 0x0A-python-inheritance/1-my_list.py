#!/usr/bin/python3
"""Class inherite the list class"""


class MyList(list):
    """class Myclass"""

    def print_sorted(self):
        """Method to sort a list"""

        s_lst = self.copy()
        s_lst.sort()
        print(s_lst)
