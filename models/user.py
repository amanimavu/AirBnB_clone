#!/usr/bin/python3
"""
module: user
resources: a super class BaseModel and a
class User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    This class inheris from BaseModel and defines
    the class variables email, password, first_name
    and last_name initialized to empty strings
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
