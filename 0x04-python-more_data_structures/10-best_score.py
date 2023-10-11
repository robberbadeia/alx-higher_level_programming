#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    _max = max(a_dictionary, key=a_dictionary.get)
    return(_max)
