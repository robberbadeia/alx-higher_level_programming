#!/usr/bin/python3
def common_elements(set_1, set_2):
    diff = set_1.difference(set_2)
    return (list(diff))
