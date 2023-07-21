#!/usr/bin/python3
"""1. Base class module"""
import json
import os
import csv

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
            if id not in Base.__id_list:
                Base.__id_list.append(id)
        else:
            Base.__nb_objects += 1
            while(Base.__nb_objects in Base.__id_list):
                Base.__nb_objects += 1
            self.id = Base.__nb_objects
            if self.id not in Base.__id_list:
                Base.__id_list.append(self.id)

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation
        of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        jsonfile = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        jsonstr = cls.to_json_string([inst.to_dictionary()
                                      for inst in list_objs])
        with open(jsonfile, "w") as f:
            f.write(jsonstr)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
            Base.just_a_dummy()
        if cls.__name__ == "Square":
            dummy = cls(1)
            Base.just_a_dummy()
        dummy.update(dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances from json file"""
        jsonfile = cls.__name__ + ".json"
        jsonstr = ""
        if not os.path.exists(jsonfile):
            return []
        with open(jsonfile, "r") as f:
            jsonstr = f.read()
        jsonlist = cls.from_json_string(jsonstr)
        return [cls.create(**inst) for inst in jsonlist]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes the JSON string representation of list_objs to a csv file"""
        csvfile = cls.__name__ + ".csv"
        if list_objs is None:
            list_objs = []
        jsonstr = cls.to_json_string([inst.to_dictionary()
                                      for inst in list_objs])
        with open(csvfile, "w", encoding='UTF8', newline='') as f:
            f.write(jsonstr)

    @classmethod
    def load_from_file_csv(cls):
        """returns a list of instances from csv file"""
        csvfile = cls.__name__ + ".csv"
        jsonstr = ""
        if not os.path.exists(csvfile):
            return []
        with open(csvfile, "r") as f:
            jsonstr = f.read()
        jsonlist = cls.from_json_string(jsonstr)
        return [cls.create(**inst) for inst in jsonlist]

    @classmethod
    def str_list(cls):
        obj_list = cls.load_from_file()
        if obj_list is None:
            return []
        str_list = []
        for element in obj_list:
            str_list.append(str(element))
        return str_list

    @classmethod
    def id_list(cls):
        "prints list of ids"
        return Base.__id_list

    @classmethod
    def id_update(cls, old_id, new_id):
        "updates the list of ids"
        if old_id not in Base.__id_list:
            return
        Base.__id_list.remove(old_id)
        Base.__init__(cls, new_id)

    @classmethod
    def id_reset(cls):
        "resets the id count"
        Base.__id_list.clear()
        Base.__nb_objects = 0

    @classmethod
    def just_a_dummy(cls):
        """ignore count for a dummy instance"""
        Base.__nb_objects -= 1