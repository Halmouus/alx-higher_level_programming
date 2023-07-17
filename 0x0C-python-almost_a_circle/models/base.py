#!/usr/bin/python3
"""1. Base class module"""


class Base:
    """class for the Base object"""
    __nb_objects = 0
    __id_list = []

    def __init__(self, id=None):
        """Instantiation with id"""
        if id is not None:
            if id < 0:
                raise ValueError("id must be positive")
            if id in Base.__id_list:
                raise ValueError(f"id ({id}) already exists")
            self.id = id
            Base.__id_list.append(id)
        else:
            Base.__nb_objects += 1
            while(Base.__nb_objects in Base.__id_list):
                Base.__nb_objects += 1
            self.id = Base.__nb_objects
            Base.__id_list.append(self.id)

    @classmethod
    def id_list(cls):
        "prints list of ids"
        print(cls.__id_list)

    @classmethod
    def id_update(cls, old_id, new_id):
        "prints list of ids"
        if old_id not in Base.__id_list:
            return
        Base.__id_list.remove(old_id)
        Base.__init__(cls, new_id)