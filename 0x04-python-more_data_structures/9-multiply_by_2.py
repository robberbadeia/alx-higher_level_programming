#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    _cp_dec = a_dictionary.copy()
    _cp_dec.update((x, y * 2) for x, y in a_dictionary.items())
    return (_cp_dec)
