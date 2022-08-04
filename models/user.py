#!/usr/bin/python3
""" User class model """
from model.base_model import BaseModel


Class User(BaseModel):
    """ Representing the User class """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
