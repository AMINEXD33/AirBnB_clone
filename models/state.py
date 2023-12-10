#!/usr/bin/python3
"""Defines the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represent a state.
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.state_id = State.state_id
        self.name = State.name
        self.__SPinit__(**kwargs)
