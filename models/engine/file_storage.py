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

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        objdict_1 = FileStorage.__objects
        objdict = {obj: objdict_1[obj].to_dict() for obj in objdict_1.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return