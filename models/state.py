#!/usr/bin/python3
"""A `State` module of users"""
from models.base_model import BaseModel


class State(BaseModel):
    """Class attribute of the state
        Args:
            name (string): state's name
        Return:
            state (object): an obj of the state
    """
    name = ""
