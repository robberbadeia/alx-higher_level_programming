#!/usr/bin/python3
"""Divide a matrix by a given number
"""


def matrix_divided(matrix, div):
    """_summary_

    Args:
        matrix (_type_): _description_
        div (_type_): _description_

    Raises:
        ZeroDivisionError: _description_
        TypeError: _description_
        TypeError: _description_
        TypeError: _description_
        TypeError: _description_
        TypeError: _description_
    """
    newMatrix = []
    rLenght = len(matrix[0])
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if (div == 0):
        raise ZeroDivisionError("division by zero")

    if (type(div) != int and type(div) != float):
        raise TypeError("div must be a number")

    if (all(type(i) is list for i in matrix) is False):
        raise TypeError("Each row of the matrix must have the same size")

    if (len(matrix) == 0):
        raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        if (len(row) != rLenght):
            raise TypeError("Each row of the matrix must have the same size")
        for el in row:
            if not isinstance(el, (int, float)):
                raise TypeError(msg)

    # Start to divide all matrix element by 2
    for row in matrix:
        lst = []
        for el in row:
            lst.append(round(el / div, 2))
        newMatrix.append(lst)
    return(newMatrix)
