#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        index = 0
        while (index < x):
            print(my_list[index], end="")
            index += 1
    except IndexError:
        pass
    print()
    return index
