#!/usr/bin/python3
"""A `City` module of of the state"""
from models.base_model import BaseModel
from models import City


class City(BaseModel):
    """The city abstract attributes
        Args:
            state_id (string): the state's id
            name (string): the name of the city
        Return:
            city (object): the city object
    """
    state_id = ""
    name = ""
