#!/usr/bin/python3
""" Defines the filestorage class."""

import json
from models.base_model import BaseModel

class FileStorage:
    """Represent an abstracted storage engine.

        __file_path (string): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        objcname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(objcname, obj.id)] = obj

 