#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    sys.argv.pop(0)
    argv_len = len(sys.argv)

    if (argv_len == 0):
        print("0 arguments.")
    elif (argv_len == 1):
        print("1 argument:")
        print("{:d}: {}".format(len(sys.argv), sys.argv[0]))
    else:
        print("{:d} arguments:".format(argv_len))
        number = 1
        for argument in sys.argv:
            print("{:d}: {}".format(number, argument))
            number += 1
