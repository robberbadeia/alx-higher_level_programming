#!/usr/bin/python3
"""
function that finds a peak in a list of unsorted integers
"""
def find_peak(list_of_integers):
    if len(list_of_integers) == 0:
        return (None)
    lenght = len(list_of_integers) - 1
    while (lenght >= 0):
        if (list_of_integers[lenght - 1] > list_of_integers[lenght] and list_of_integers[lenght - 1] > list_of_integers[lenght - 2]):
            return list_of_integers[lenght - 1]
        lenght -= 1
