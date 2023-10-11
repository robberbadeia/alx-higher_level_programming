#!/usr/bin/python3
def best_score(a_dictionary):
	_sorted = dict(sorted(a_dictionary.items()))
	return (_sorted.key[len(_sorted) - 1])