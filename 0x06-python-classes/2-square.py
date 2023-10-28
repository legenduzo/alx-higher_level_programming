#!/usr/bin/python3

"""Module documentation for 2-square.py

This module implements size for a square class
"""


class Square:
    """Represents a square

    A class used to represent a square

    Attributes:
        size (int): size of the square
    """
    def __init__(self, size=0):
        """__init__ method for the square class

        Args:
            size (int): size must be greater than 0
        """
        self.size = size

        @property
        def size(self):
            """private property with getter and setter

            size has to be > 0 and must be an int
            """
            return self.__size

        @size.setter
        def size(self, size):
            if not isinstance(size, int):
                raise TypeError('size must be an integer')
            elif size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
