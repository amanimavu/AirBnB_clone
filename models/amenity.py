#!/usr/bin/python3
"""
module: amenity
resources: the BaseModel class as super class
and Amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    This class is used to define the Amenity
    objects. It contains a class variable name
    """
    name = ""
