#!/usr/bin/python3
"""1. Base class module"""
import json


class Base:
    """class for the Base object"""
    __nb_objects = 0
    __id_list = []

    def __init__(self, id=None):
        """Instantiation with id"""
        if id is not None:
            if not isinstance(id, int):
                raise TypeError("id must be an integer")
            if id < 0:
                raise ValueError("id must be positive")
            self.id = id
            Base.__id_list.append(id)
        else:
            Base.__nb_objects += 1
            while(Base.__nb_objects in Base.__id_list):
                Base.__nb_objects += 1
            self.id = Base.__nb_objects
            Base.__id_list.append(self.id)

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation
        of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
        

    @classmethod
    def id_list(cls):
        "prints list of ids"
        return Base.__id_list

    @classmethod
    def id_update(cls, old_id, new_id):
        "prints list of ids"
        if old_id not in Base.__id_list:
            return
        Base.__id_list.remove(old_id)
        Base.__init__(cls, new_id)