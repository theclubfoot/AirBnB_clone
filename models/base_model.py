#!/usr/bin/python3
""" Base Class module
This module contains all the attributes and methods
 of the Base Class for the AirBnB clone webapp
"""

from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """ Base model class with its hierarchy """

    def __init__(self, *args, **kwargs):
        """ Initializes the base class

        Arguments:
           - *args: list of arguments
            - **kwargs: dict of key-value pair arguments
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.datetime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ Returns a string representation of an instance """

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """ saves the 'update_at' attribute with
         the current datetime. """

        self.update_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns a dictionary representation of an instance. """

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
