#!/usr/bin/python3
"""Function to write a text into a file"""


def write_file(filename="", text=""):
    """Function implementation"""

    with open(filename, "w", encoding="utf-8") as file:
        nb = file.write(text)
        return(nb)
