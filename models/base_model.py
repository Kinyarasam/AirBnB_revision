#!/usr/bin/python3
"""This module defines the base class for all models in this project"""
from uuid import uuid4
from datetime import datetime as dt


class BaseModel():
    """defines all common attributes for other classes"""
    def __init__(self):
        """Initialize a new Base
        
        Args:
            id (int): identity of the new Base
            created_at (str):
        """
        self.id = str(uuid4())
        self.created_at = dt.now()
        self.updated_at = dt.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        return '[{}] ({}) {}'.format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance updated_at"""
        self.updated_at = dt.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        temp = dict(self.__dict__)
        temp['__class__'] = self.__class__.__name__
        temp['updated_at'] = self.updated_at.strftime(
                "%Y-%m-%dT%H:%M:%S.%f")
        temp['created_at'] = self.created_at.strftime(
                '%Y-%m-%dT%H:%M:%S.%f')
        return temp
