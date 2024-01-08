#!/usr/bin/python3
"""inherst from"""


def inherits_from(obj, a_class):
    """
    Args:
        obj: object
        a_class: class

    Returns:
        True or fals
    """
    if type(obj) == a_class or isinstance(obj, a_class):
        return True
    else:
        return False
