#!/usr/bin/python3
def print_last_digit(number):
    lst = abs(number) % 10
    print("{}".format(lst), end='')
    return (lst)
