#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    ln = len(argv) - 1
    if (ln == 0):
        print("{} argument.".format(ln))
    elif (ln == 1):
        print("{} argument:".format(ln))
    else:
        print("{} arguments:".format(ln))
