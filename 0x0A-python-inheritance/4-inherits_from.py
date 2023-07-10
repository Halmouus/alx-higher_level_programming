#!/usr/bin/python3
"""4. Only sub class of

function that returnsTrue if the object is an instance of a class
that inherited (directly or indirectly) from the specified class;
otherwise False."""


def inherits_from(obj, a_class):
    """function that returnsTrue if the object is an instance of
    a class that inherited (directly or indirectly) from the specified
    class; otherwise False.

    obj : the object to be checked
    a_class : class to be check
    return: True if the object is an instance of a class that inherited
    from, the specified classs ; otherwise False
    """
    return isinstance(obj, a_class) and (type(obj) is not a_class)
