#!/usr/bin/python3

"""Say my name

Prints the name provided
"""

def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>"
    Raises a TypeError if spec is not met

    Args:
        first_name (str): the first name
        last_name (str, optional): the last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
