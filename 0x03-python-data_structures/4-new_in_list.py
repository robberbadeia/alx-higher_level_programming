#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_lst = my_list.copy()
    if (idx < 0):
        return new_lst
    if (idx >= len(new_lst)):
        return new_lst
    if (new_lst):
        new_lst[idx] = element
        return new_lst
