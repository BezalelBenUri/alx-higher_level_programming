#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Class that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a Square instance"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method to retrieve the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size attribute"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Getter method to retrieve the position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method to set the position attribute"""
        if type(value) != tuple or len(value) != 2 or \
           type(value[0]) != int or type(value[1]) != int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the area of the square"""
        return self.size ** 2

    def my_print(self):
        """Prints the square with the character #"""
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        """Returns a string representation of the Square"""
        output = ""
        if self.size == 0:
            return output
        else:
            for _ in range(self.position[1]):
                output += '\n'
            for _ in range(self.size):
                output += " " * self.position[0] + "#" * self.size + '\n'
            return output[:-1]
