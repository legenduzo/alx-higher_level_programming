#!/usr/bin/python3
import json
"""Object to Json Module"""


def to_json_string(my_obj):
    """Converts object to json sting

    Args:
        my_object (py object): object to convert

    Return:
        json
    """
    return json.dumps(my_obj)
