#!/usr/bin/python3
"""2. Exact same object

function that returns True if the object is exactly
an instance of the specified class ; otherwise False"""


def is_same_class(obj, a_class):
    """function that returns True if the object is exactly
    an instance of the specified class ; otherwise False

    obj : the object to be checked
    a_class : class to be check
    return: True if the object is exactly
    an instance of the specified class ; otherwise False
    """
    return type(obj) is a_class

