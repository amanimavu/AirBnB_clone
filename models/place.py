#!/usr/bin/python3
"""
module: place
resources: a super class BaseModel and class
named Place
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    This class inherits from BaseModel and defines
    the class variables city, user_id, name,
    description, number_rooms, max_guest, latitude,
    longitude, price_by_night and amenity_ids.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_of_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
