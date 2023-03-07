#!/usr/bin/python3
"""
module: review
resources: a super class BaseModel and a
class Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    This class inherits from the class BaseModel.
    It defines the class variables, place_id,
    user_id and text initialized to empty strings
    """
    place_id = ""
    user_id = ""
    text = ""
