#!/usr/bin/python3
def cal(argv):
    print(len(argv))
    if (len(argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])

        if (argv[2] == '+'):
            result = add(a, b)
            print("{} + {} = {}".format(a, b, result))
        elif (argv[2] == '-'):
            result = sub(a, b)
            print("{} - {} = {}".format(a, b, result))
        elif (argv[2] == "*"):
            result = mul(a, b)
            print("{} * {} = {}".format(a, b, result))
        elif (argv[2] == '/'):
            result = div(a, b)
            print("{} / {} = {}".format(a, b, result))


if __name__ == "__main__":
    from calculator_1 import add, div, mul, sub
    from sys import argv
    cal(argv)
