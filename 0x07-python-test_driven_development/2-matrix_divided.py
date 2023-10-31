#!/usr/bin/python3
"""Matrix module

This module divides an int or float matrix
"""


def matrix_divided(matrix, div):
    """
    Function to divide all elements of a matrix by a divider.

    Args:
        matrix (list): A matrix (list of lists) of numbers
        div (int/float): A number (int/float), the divider.

    Raises:
        TypeError: If type specs are not met
        ZeroDivisionError: If div is 0.

    Returns:
        list: New matrix with all elements divided
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a list of lists of integers/floats")
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("matrix must be a list of lists of integers/floats")
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    return [[round(item / div, 2) for item in row] for row in matrix]
