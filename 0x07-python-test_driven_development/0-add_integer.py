#!/usr/bin/python3
"""Add integer module

Adds integers and floats alone
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int, float): The first integer to be added.
        b (int, float): The second integer to be added.

    Returns:
        int: The result of the addition between a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
