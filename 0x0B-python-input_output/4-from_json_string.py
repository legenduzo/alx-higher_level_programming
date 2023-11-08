#!/usr/bin/python3
import json
"""To Json Module"""


def from_json_string(my_obj):
    """converts object to json string

    Args:
        my_obj (py obj): object to convert

    Return:
        Json
    """
    return json.loads(my_obj)
