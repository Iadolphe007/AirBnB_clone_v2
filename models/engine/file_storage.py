#!/usr/bin/python3
"""file storage module"""
import json


class FileStorage:
    """class manage JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def delete(self, obj=None):
        """delete method"""
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if key in self.__objects:
                del self.__objects[key]

    def all(self, cls=None):
        """returns the list of objects"""
        if cls is None:
            return self.__objects
        else:
            filterd_objs = {
                    key: obj
                    for key, obj
                    in self.__objects.items()
                    if isinstance(obj, cls)
                    }
            return filterd_objs

    def new(self, obj):
        """Adds object to storage dict"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dict"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dict"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass