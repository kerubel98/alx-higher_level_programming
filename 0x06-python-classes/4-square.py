#!/usr/bin/python3
"""square class"""


class Square:
    """Square definition"""

    def __init__(self, size=0):
        """Constructor

        Args:
            size: size of sides

        Raises:
            ValueError: if size < 0
            TypeError: if size is not an integer
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Area of a square

        Return:
            the size squared
        """
        return self.__size ** 2


    @property
    def size(self):
        """size gater mathod

        Returns:
            the size of squar
        """

        return self.__size


    @size.setter
    def size(self, value):
        """size sater mathod

        Args:
            value: the value of sides
        Raises:
            TaypError: if size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
