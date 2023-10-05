if __name__ == "__main__":
    import sys

    ln = len(sys.argv) - 1
    if (ln == 0):
        print("{} argument.".format(ln))
    elif (ln == 1):
        print("{} argument:".format(ln))
    else:
        print("{} arguments:".format(ln))
    i = 1
    for arg in sys.argv:
        print("{:d}:{}".format(i,arg))
                
                