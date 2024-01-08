#!/usr/bin/python3
"""isnstance of class"""


def is_same_class(obj, a_class):
    """
    Args:
        obj: object
        a_class: calss

    Returns: true if obj is instance of a_class
    """

    if type(obj) == a_class:
        return True
    else:
        return False
