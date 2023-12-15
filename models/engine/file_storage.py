#!/usr/bin/python3

"""Class that store first object"""
import json
import os


class FileStorage:
    """This that serializes instances to a JSON
    file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, "w") as f:
            my_dict = {
                key: value.to_dict()
                for key, value in self.__objects.items()
            }
            json.dump(my_dict, f)

    def handle_import(self):
        """Function to handler circular import"""
        from models.base_model import BaseModel
        from models.user import User
        cls_name = {
            "BaseModel": BaseModel,
            "User": User
        }
        return (cls_name)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists,
        otherwise, do nothing.
        """

        if not os.path.isfile(self.__file_path):
            return
        with open(self.__file_path, "r") as f:
            my_dict2 = json.load(f)
            my_dict2 = {
                key: self.handle_import()[value["__class__"]](**value)
                for key, value in my_dict2.items()
            }
            self.__objects = my_dict2
