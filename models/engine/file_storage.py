#!/usr/bin/python3
"""Defines the FileStorage class."""
import sys
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine.
    """
    __file_path = absolute_path = os.path.abspath("./models/engine/file.json")
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def save(self):
        """save
            serialize the objects to json and store them
            in the __file_path
        """
        # load all the objects in the dict to json
        new_obj_dict = {}
        for x in FileStorage.__objects.keys():
            # add to the new dict the same key, but for the value
            # load it with the object to_dict (see base_model)
            new_obj_dict[x] = FileStorage.__objects[x].to_dict()
        # ++++DEBUGING++++++
        # print ("what are you saving ", new_obj_dict)
        # save the loaded json txt to the __file_path
        try:
            with open(FileStorage.__file_path, 'w') as file:
                # write to the file
                json.dump(new_obj_dict, file)
        except Exception:
            pass

    def reload(self):
        """reload
            from the file reload all the json objects to memorie
        """
        def set_value_for_sub_classes(obj, list_, val):
            """set_value_for_sub_classes
            args:
                obj: the target object
                list_: list of attributes to set
                val: a dict containing the attributes name and values
            """
            for x in list_:
                try:
                    setattr(obj, x, val[x])
                except Exception:
                    print("can't set ", x, "for", bj)
        try:
            with open(FileStorage.__file_path) as file:
                # load opject into dict
                loaded_dict = json.load(file)
                for val in loaded_dict.values():
                    cls_name = val["__class__"]
                    del val["__class__"]
                    # only import the base_model when it's needed
                    from models import base_model
                    # using the dict to initialize the new instance
                    obj = eval(cls_name)(**val)
                    # set the specific attributes for some instance#####
                    if (cls_name == "User"):
                        set_value_for_sub_classes(obj, ["email",
                                                        "password",
                                                        "first_name",
                                                        "last_name"],
                                                  val)
                    elif (cls_name == "State"):
                        set_value_for_sub_classes(obj, ["name"],
                                                  val)
                    elif (cls_name == "City"):
                        set_value_for_sub_classes(obj, ["state_id",
                                                        "name"],
                                                  val)
                    elif (cls_name == "Amenity"):
                        set_value_for_sub_classes(obj, ["name"],
                                                  val)
                    elif (cls_name == "Place"):
                        set_value_for_sub_classes(obj,
                                                  ["city_id",
                                                   "user_id",
                                                   "name",
                                                   "description",
                                                   "number_rooms",
                                                   "number_bathrooms",
                                                   "max_guest",
                                                   "price_by_night",
                                                   "latitude",
                                                   "longitude",
                                                   "amenity_ids"],
                                                  val)
                    elif (cls_name == "Review"):
                        set_value_for_sub_classes(obj,
                                                  ["place_id",
                                                   "user_id",
                                                   "text"],
                                                  val)
                            
                    # create the new object
                    self.new(obj)
        except Exception:
            pass

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def flush(self):
        """flush
            reset the dict to empty
        """
        FileStorage.__objects = {}

    def flush_key(self, key):
        """flush_key
            delets a specific key_value from the dict
        """
        if key in FileStorage.__objects:
            del FileStorage.__objects[key]
