#!/usr/bin/python3
"""
This module provides a function to print a square using '#'.

Functions:
print_square(size): Prints a square of given size using '#'.
"""


def print_square(size):
    """Prints a square with the character #

    Args:
    size (int): The size length of the square

    Raises:
    TypeError: If size is not integer
    ValueError: If size is less than 0

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    else:
        for i in range(size):
            print("#" * size)
