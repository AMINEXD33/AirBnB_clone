#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent an Place.
    Atttibutes:
        city_id (str): the id of the city
        name (str): name of the Place
        description (str): discription of the place
        number_rooms (int): number of rooms
        number_bathrooms (int): number of bathrooms
        max_guest (int): max number of guests at one go
        price_by_night (int):....
        latitude (float): ....
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
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.city_id = Place.city_id
        self.user_id = Place.user_id
        self.name = Place.name
        self.description = Place.description
        self.number_rooms = Place.number_rooms
        self.number_bathrooms = Place.number_bathrooms
        self.max_guest = Place.max_guest
        self.price_by_night = Place.price_by_night
        self.latitude = Place.latitude
        self.longitude = Place.longitude
        self.amenity_ids = Place.amenity_ids

        self.__SPinit__(**kwargs)
