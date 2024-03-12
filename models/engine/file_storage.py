#!/usr/bin/python3



import json
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """FileStorage class for serialization and deserialization of models."""

    def __init__(self):
        """Initialize a new FileStorage instance."""
        self.file_path = "file.json"
        self.objects = {}

    def all(self, cls=None):
        """Return all objects of a given class."""
        if cls is None:
            return list(self.objects.values())
        return [obj for obj in self.objects.values() if isinstance(obj, cls)]

    def new(self, obj):
        """Add a new object to the file storage."""
        if isinstance(obj, BaseModel):
            if obj.id is None:
                obj.id = len(self.objects) + 1
            self.objects[obj.id] = obj
            self.save()
            return obj
        raise TypeError("Object is not a subclass of BaseModel")

    def save(self):
        """Save all objects to the file."""
        with open(self.file_path, "w") as file:
            json.dump([obj.__dict__ for obj in self.objects.values()], file)

    def load(self):
        """Load all objects from the file."""
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                for obj_data in data:
                    obj_class = globals()[obj_data["__class__"]]
                    obj = obj_class(**obj_data)
                    self.objects[obj.id] = obj
        except FileNotFoundError:
            pass

    def delete(self, obj):
        """Delete an object from the file storage."""
        if isinstance(obj, BaseModel):
            del self.objects[obj.id]
            self.save()
