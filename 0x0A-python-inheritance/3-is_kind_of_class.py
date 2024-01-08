#!/usr/bin/python3
"""function check class"""


def is_kind_of_class(obj, a_class):
    """chacke obj instance for class

    Args:
        obj: object
        a_class: class
    Restuens:
        true is obj is insatnce of a_class
    """
    return isinstance(obj, a_class)
