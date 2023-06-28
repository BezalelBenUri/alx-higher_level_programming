#!/usr/bin/python3


 """Represent a square."""


class Square:
    """Class that defines a square"""

    def __init__(self, size=0):
        """Initializes a Square instance with an optional size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
