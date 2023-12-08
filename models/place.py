#!/usr/bin/python3
"""A `Place` module of users"""
from models.base_model import BaseModel
from models import User
from models import Amenity


class Place(BaseModel):
    """ A class abstracting places
        Args:
            city_id (string): city's id
            user_id (string): user's id
            name (string): name of the place
            description (string): description of the plce
            number_rooms (string): number of rooms
            number_bathrooms (string): number of bathrooms
            max_guest (int): maximum number of guest
            price_by_night (int): price pair night of visit
            latitude (float): place latitude
            longitude (float): place longitude
            amenity_ids (list): the features of the place
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = {}
