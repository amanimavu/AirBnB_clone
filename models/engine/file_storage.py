#!/usr/bin/python3

"""
module: file_storage
resources: class named FileStorage
"""
import json
from datetime import datetime


class FileStorage:
    """
    This class serializes instances to a JSON file and deserializes
    JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        This method returns the dictionary __objects that
        stores instances created
        """
        return type(self).__objects

    def new(self, obj):
        """
        This method is used to store an instance that has
        been created to the dictionary __objects
        """
        obj_cls_name = obj.__class__.__name__
        obj_id = obj.__dict__["id"]
        object_key = "{}.{}".format(obj_cls_name, obj_id)
        type(self).__objects[object_key] = obj

    def save(self):
        """
        This method is used to serialize a copy of the
        python dictionary to a specific file. This is
        to make the console program persistent.
        """
        with open(type(self).__file_path, "w") as file:
            new_objects = {}
            for key, value in type(self).__objects.items():
                new_objects[key] = value.to_dict()
            json.dump(new_objects, file)

    def reload(self):
        """
        This method is to deserializes the json string
        from a file to a python dictionary. This also
        help to make the console program persistent
        """
        from models.user import User
        from models.base_model import BaseModel
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.amenity import Amenity
        try:
            file = open(type(self).__file_path)
        except FileNotFoundError:
            pass
        else:
            try:
                saved_objs = json.load(file)
            except Exception:
                print("file can't be loaded")
            else:
                for key, value in saved_objs.items():
                    cls = locals()[value["__class__"]]
                    type(self).__objects[key] = cls(**value)
            finally:
                file.close()
