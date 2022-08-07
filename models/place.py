#!/usr/bin/python3
""" Place Class Model """
from model.base_model import BaseModel


Place User(BaseModel):
    """ Representing the Place class """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_bathroom = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
