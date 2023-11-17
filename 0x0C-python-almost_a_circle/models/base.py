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

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string
        representation json_string
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation
        of list_objs to a file
        """
        file = '{}.json'.format(cls.__name__)
        with open(file, 'w') as f:
            if not list_objs:
                f.write('[]')
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(list_dicts))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        dummy = cls(**dictionary)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        file = '{}.json'.format(cls.__name__)
        newlist = []
        try:
            with open(file, 'r') as f:
                new = cls.from_json_string(f.read())
                for dictionary in new:
                    newlist.append(cls.create(**dictionary))
                return newlist
        except FileNotFoundError:
            return []
