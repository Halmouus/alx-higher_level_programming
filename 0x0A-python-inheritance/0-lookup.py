#!/usr/bin/python3
"""0. Lookup

a function that returns the list of available
attributes and methods of an object"""


def lookup(obj):
    """function that returns the list of available
    attributes and methods of an object

    obj : the object whose attributes and methods
    are to be listed
    return: a list object
    """
    return dir(obj)
