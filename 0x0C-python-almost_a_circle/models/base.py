#!/usr/bin/python3
"""Base Module
"""
import json


class Base:
    """Base class

    Attributes:
        __nb_objects (int): provate class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """init method

        Initializes the class

        Args:
            id: keyword argument
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dict to JSON and returns it"""
        if not list_dictionaries:
            return '[]'
        return json.dumps(list_dictionaries)
