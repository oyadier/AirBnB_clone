#!/usr/bin/python3

"""This is a base class model"""
import uuid
from datetime import datetime


class BaseModel:
    """The class attributes"""

    def __init__(self):
        """Initialize an instance of `BaseModel`

            Args:
                id (str): the unique id of an instance
                created_at (datetime): the date and time instance is created
                update_at (datetime): the data and time
                                instance is created or updated
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return a string representation of the object"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__))

    def save(self):
        """Update newly updated data and time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        key = self.__dict__.copy()
        key['__class__'] = self.__class__.__name__
        key['created_at'] = self.created_at.isoformat()
        key['updated_at'] = self.updated_at.isoformat()
        return key
