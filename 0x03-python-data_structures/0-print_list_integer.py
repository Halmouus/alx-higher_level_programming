#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if not (my_list is None):
        for i in my_list:
            print("{:d}".format(i))
