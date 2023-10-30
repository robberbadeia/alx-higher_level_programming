#!/usr/bin/python3
import sys
def argChecker(args):
    """ Check the ARGS"""
    if len(args) < 2 or len(args) > 2:
        print ("Usage: nqueens N")
        exit(1)

    if not args[1].isdigit():
        print("N must be a number")
        exit(1)

    if (int(args[1]) < 4):
        print("N must be at least 4")
        exit(1)




if __name__ == "__main__":
    args = sys.argv
    argChecker(args)
