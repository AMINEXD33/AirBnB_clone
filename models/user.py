#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User.

    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""    
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs) 
        self.email = User.email
        self.password = User.password
        self.first_name = User.first_name
        self.last_name = User.last_name
        self.__SPinit__(**kwargs)
