#!/usr/bin/python3
""" Base class Module"""

import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        String representation of the class
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute updated_at with the
        current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        ndict = self.__dict__.copy()
        ndict["__class__"] = self.__class__.__name__
        ndict["created_at"] = datetime.isoformat(self.created_at)
        ndict["updated_at"] = datetime.isoformat(self.updated_at)
        return ndict
