#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for i in range(x):
            if(i.isdigit())
                print("{:d}".format(my_list[i]), end="")
    except IndexError:
        print("list index out of range")
