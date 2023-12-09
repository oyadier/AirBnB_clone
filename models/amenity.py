#!/usr/bin/python3
"""A `Amenity` module of place"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """A class attributes
        Args:
            name (string): amenity's name
        Return:
        amenity (obj): amenity object
    """
    name = ""
