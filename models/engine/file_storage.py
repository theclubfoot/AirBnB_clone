#!/usr/bin/python3
""" FileStorage class module. """

import datetime
import json
import os


class FileStorage:
    """ Class object for serialization and deserialization of base classes """
    __file_name = "file.json"
    __objects = {}

    def all(self):
        """ Method to return all objects '__objects' dictionary """
        return FileStorage.__objects

    def new(self, obj):
        """ Create new objects 'obj' in __objects dictionary """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.objects[key] = obj

    def save(self):
        """ Serializes objects '__objects' to JSON file """
        with open(FileStorage.__file_name, "w", encoding="utf-8") as file:
            data = {key: value.to_dict() for key, value
                    in FileStorage.__objects.items()}
            json.dump(data, file)

    def classes(self):
        """ Return a dictionary of valid classes and their id references. """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        """ Deserializes JSON file into objects '__objects' dictionary """"
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_name, "r", encoding="utf-8") as file:
            obj_dict = json.load(file)
            obj_dict = {key: self.classes()[value["__class__"]](**value)
                        for key, value in obj_dict.items()}
            FileStorage.__objects = obj_dict

    def attribues(self):
        """ Returns all attributes and their valid types for classname. """
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      " price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes
