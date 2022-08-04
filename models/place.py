#!/usr/bin/python3
""" Place Class Model """
from model.base_model import BaseModel


Place User(BaseModel):
    """ Representing the Place class """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_bathroom = ""
    max_guest = ""
    price_by_night = ""
    latitude = ""
    longitude = ""
    amenity_ids = ""
