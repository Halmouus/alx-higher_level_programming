#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    i = 0
    for c in str:
        if i == n:
            i += 1
            continue
        new_str += c
        i += 1
    return new_str
