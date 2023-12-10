#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel

class Review(BaseModel):
    """Represent a Review.
    """
    place_id = ""
    user_id = ""
    text = ""    
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.place_id = Review.place_id
        self.user_id = Review.user_id
        self.text = Review.text
        self.__SPinit__(**kwargs)    
