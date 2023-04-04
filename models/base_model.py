#!/usr/bin/python3
""" Base Model Module"""

import cmd
import uuid
from datetime import datetime


class BaseModel:
    """ Defines BaseModel class

    Args:
        id (str): uuid generated unique id
        created_at: current datetime instance was created
        updated_at: current datetime instance was updated

    Attributes:
        None
    """
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs is not None:
            for k,v in kwargs.items():
                if k == 'id':
                    self.id = v
                elif k == 'created_at':
                    self.created_at = self.created_at.fromisoformat(v)
                elif k == 'updated_at':
                    self.updated_at = self.updated_at.fromisoformat(v)


    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        instanceDict = self.__dict__
        instanceDict['__class__'] = self.__class__.__name__
        instanceDict['created_at'] = self.created_at.isoformat()
        instanceDict['updated_at'] = self.updated_at.isoformat()
        return instanceDict

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
