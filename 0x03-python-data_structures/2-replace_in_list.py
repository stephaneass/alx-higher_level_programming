#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    length = len(my_list) - 1
    if (0 <= idx and idx <= length):
        my_list[idx] = element
    return (my_list)
