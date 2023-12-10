#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent a Amenity.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.name = Amenity.name
        self.__SPinit__(**kwargs)
