#!/usr/bin/python3
"""rectangel class"""


class Rectangle:
    """class defination """
    def __init__(self, width=0, height=0):

        """Args:
                width
                height
            Raises:
                TypeError: if width or height not integer
                ValueError: if width or height less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.width = value

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.height = value
