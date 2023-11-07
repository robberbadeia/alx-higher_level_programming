#!/usr/bin/python3
"""Pascal Triangle"""


def pascal_triangle(n):
    """Function Implementation"""
    for i in range(1,n + 1):  
        m = 1;  
        for j in range(1,i + 1):
            print(m, end = " ")
            m = int(m * (i - j) / j)  
        print("")
