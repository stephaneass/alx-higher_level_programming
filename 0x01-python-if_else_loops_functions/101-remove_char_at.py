#!/usr/bin/python3
def remove_char_at(str, n):
    data = ''
    i = 0
    for c in str:
        if i != n:
            data += str[i]
        i += 1
    return data
