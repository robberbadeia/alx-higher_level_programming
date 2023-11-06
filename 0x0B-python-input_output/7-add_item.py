#!/usr/bin/python3
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
import sys
"""Script to adds all arguments to a Python list
    and then save them to a file
"""

if __name__ == "__main__":
    filename = "add_item.json"
    data = load_from_json_file(filename)
    for arg in sys.argv[1:]:
        data.append(arg)

    save_to_json_file(data, filename)
