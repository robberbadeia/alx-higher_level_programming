#!/usr/bin/python3
import json
"""creates an Object from a "JSON file"""


def load_from_json_file(filename):
    """Function Implementation"""

    with open(filename) as file:
        return json.load(file)
