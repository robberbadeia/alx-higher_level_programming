#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if (matrix):
        for row in matrix:
            for j in range(len(row)):
                if (j < (len(row) - 1)):
                    print("{}".format(row[j]), end=' ')
                else:
                    print("{}$".format(row[j]), end='')
            print("")
