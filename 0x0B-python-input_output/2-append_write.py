#!/usr/bin/python3
"""Function to append text to a file"""


def append_write(filename="", text=""):
    """Function Implementation"""

    with open(filename, 'a', encoding="utf-8") as file:
        nb = file.write(text)
        return(nb)
