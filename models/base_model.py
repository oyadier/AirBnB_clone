#!/usr/bin/python3

"""This is a base class model"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """The class attributes"""

    def __init__(self, *args, **kwargs):
        """Initialize an instance of `BaseModel`

            Args:
                id (str): the unique id of an instance
                created_at (datetime): the date and time instance is created
                update_at (datetime): the data and time
                                instance is created or updated
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
                            )
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
                            )
                else:
                    self.__dict__[key] = kwargs[key]

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return a string representation of the object"""
        return ("[{}] ({}) {}".format(type(self).__name__,
                self.id, self.__dict__))

    def save(self):
        """Update newly updated data and time"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        key = self.__dict__.copy()
        key['__class__'] = type(self).__name__
        key['created_at'] = key["created_at"].isoformat()
        key['updated_at'] = key["updated_at"].isoformat()
        return key
