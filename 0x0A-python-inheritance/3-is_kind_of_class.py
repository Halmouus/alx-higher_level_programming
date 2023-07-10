#!/usr/bin/python3
"""3. Same class or inherit from

function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False"""


def is_kind_of_class(obj, a_class):
    """function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False

    obj : the object to be checked
    a_class : class to be check
    return: True if the object is an instance of a class that inherited
    from, the specified classs ; otherwise False
    """
    return isinstance(obj, a_class)
