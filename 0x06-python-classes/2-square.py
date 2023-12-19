#!/usr/bin/python3
"""square calss"""


class Square:
    """class defination"""

    def __init(self, size=0):
        """constractor 

        Args:
            size: length of the side
        Raises:
            TypeError: if the size is not integer
            ValueError: if the size is < zero
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self__size = size
