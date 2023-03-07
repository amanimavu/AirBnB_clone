#!/usr/bin/python3
"""
module: state
resources: a super class called BaseModel
and a class State
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    This class inherits from a class BaseModel
    and defines a unique class variable name
    that initializes to an empty string
    """
    name = ""
