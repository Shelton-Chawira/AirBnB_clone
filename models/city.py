#!/usr/bin/python3

"""
Module for the City class.
"""

from models.base_model import BaseModel
from models.state import State

class City(BaseModel):
    """Representation of a City."""

    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new City instance."""
        super().__init__(*args, **kwargs)
        self.state_id = kwargs.get("state_id", None)
        self.state = None
        if self.state_id:
            self.state = State.objects.get(id=self.state_id)
