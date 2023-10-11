#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
	_keys = list(a_dictionary.keys())
	_keys.sort()
	_sorted_dic = {i: a_dictionary[i] for i in _keys}
	for key, val in _sorted_dic.items():
		print("{}: {}".format(key, val))
