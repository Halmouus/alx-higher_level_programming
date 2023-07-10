#!/usr/bin/python3
"""1. My list"""


class MyList(list):
    """a class MyList that inherits from list"""
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
