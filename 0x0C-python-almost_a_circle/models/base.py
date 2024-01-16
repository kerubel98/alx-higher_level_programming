#!/usr/bin/python3
"""Module holeds class base"""


class Base:
    """class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor
        Args:
            id:instance argument
        """
        if id is  None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
