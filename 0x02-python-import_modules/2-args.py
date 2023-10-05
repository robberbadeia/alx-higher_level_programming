#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    ln = len(sys.argv) - 1
    if (ln == 0):
        print("{} argument.".format(ln))
    elif (ln == 1):
        print("{} argument:".format(ln))
    else:
        print("{} arguments:".format(ln))
    for i in range(ln):
        print("{:d}:{}".format((sys.argv + 1), sys.args[i + 1]))
