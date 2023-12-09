#!/usr/bin/python3
"""This is a `Review Module` for reviewing places"""r
from models.base_model import BaseModel


class Review(BaseModel):
    """A class  attributes of the Review

        Args:
            place_id (string): the place's id
            user_id (string): the user's id
            text (string): the user's review comment

        Return:
            review (string): the commented text
    """
    place_id = ""
    user_id = ""
    text = ""
