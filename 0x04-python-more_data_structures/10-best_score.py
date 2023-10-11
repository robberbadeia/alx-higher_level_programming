#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary is None):
        return None
    _max = max(a_dictionary, key=a_dictionary.get)
    return(_max)
