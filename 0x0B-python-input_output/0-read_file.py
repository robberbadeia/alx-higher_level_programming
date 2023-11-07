#!/usr/bin/python3
"""Function to read from a file and print text"""


def read_file(filename=""):
    """Function Implementation"""

    with open(filename, encoding="utf-8") as file:
        text = file.read()
        print(text)
