#!/usr/bin/python3

"""
Module for the Review class.
"""

from models.base_model import BaseModel
from models.place import Place
from models.user import User

class Review(BaseModel):
    """Representation of a Review."""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new Review instance."""
        super().__init__(*args, **kwargs)
        self.place_id = kwargs.get("place_id", None)
        self.place = None
        if self.place_id:
            self.place = Place.objects.get(id=self.place_id)
        self.user_id = kwargs.get("user_id", None)
        self.user = None
        if self.user_id:
            self.user = User.objects.get(id=self.user_id)
