#!/usr/bin/python3

"""
Module for the Place class.
"""

from models.base_model import BaseModel
from models.city import City
from models.user import User

class Place(BaseModel):
    """Representation of a Place."""

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
        """Initialize a new Place instance."""
        super().__init__(*args, **kwargs)
        self.city_id = kwargs.get("city_id", None)
        self.city = None
        if self.city_id:
            self.city = City.objects.get(id=self.city_id)
        self.user_id = kwargs.get("user_id", None)
        self.user = None
        if self.user_id:
            self.user = User.objects.get(id=self.user_id)
