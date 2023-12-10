#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city.

    Atttibutes:
        name (str): name of the city
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.state_id = City.state_id
        self.name = City.name
        self.__SPinit__(**kwargs)
