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
    def __init__(self, size=0, position=(0, 0)):
        """__init__ method for the square class

        Args:
            size (int): size must be greater than 0
            position (tuple): determines the position square starts from.
            First arg sets side, second arg sets top
        """
        self.size = size
        self.position = position

    @property
    def position(self):
        """private property with getter and setter

        position determines where square starts from
        """
        return self.__position

    @position.setter
    def position(self, position):
        if position[0] < 0 or position[1] < 0 or len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = position

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

    def area(self):
        """Area method

        Returns:
            The area of the square
        """
        return self.size * self.size

    def my_print(self):
        """Prints # to the standard output

        If self.size = 0, prints nothing
        """
        if self.size > 0:
            for i in range(0, self.position[1]):
                print('\n', end='')
            for i in range(0, self.size):
                print(' ' * self.position[0] + '#' * self.size)
        else:
            print()
