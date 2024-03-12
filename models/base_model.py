#!/usr/bin/python3

"""
    BaseModel module
"""

import uuid
from datetime import datetime
import file_storage

class BaseModel:
    def __init__(self, *args, **kwargs):
    if kwargs:
        for key, value in kwargs.items():
            if key != "__class__":
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)
        self.updated_at = datetime.now()
    else:
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    file_storage.FileStorage().new(self)

    def save(self):
        self.updated_at = datetime.now()
        file_storage.FileStorage().save()

    def to_dict(self):
        data = self.__dict__.copy()
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        data['__class__'] = self.__class__.__name__
        return data

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
