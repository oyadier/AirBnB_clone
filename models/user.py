#!/usr/bin/python3
"""This module class `User` abstract users of the system"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class abstrating system users

        Args:
            email (string): user's email
            password (string): user's password
            first_name (string): user's first name
            last_name (string): user's last name

        Return:
            obj (object): the object of a newly create user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
