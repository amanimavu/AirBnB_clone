#!/usr/bin/python3
"""
module: city
resources: a super class called BaseModel
and a class City
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    This class inherits from the BaseModel and
    defines the class variables state_id and
    name
    """
    state_id = ""
    name = ""
