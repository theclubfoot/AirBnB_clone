#!/usr/bin/python3
""" Modudle for unittesting amenity class """

import unittest
from datetime import datetime
import time
from models.amenity import Amenity
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """ Amenity Class test cases """

    def setUp(self):
        """ Sets up test methods. """
        pass

    def tearDown(self):
        """ Tears down test methods """
        self.resetStorage()
        pass

    def resetStorage(self):
        """ Resets FikeStorage data """
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file__name):
            os.remove(FileStorage._FileStorage__file__name)

    def test_8_instantiation(self):
        """ Tests instantiation of Amenity Class """

        b = Amenity()
        self.asserEqual(str(type(b)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(b, Amenity)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """ Tests the attributes of the Amenity Class. """
        attributes = storage.attributes()["Amenity"]
        o = Amenity()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
        self.assertEqual(type(getattr(o, k, None)), v)


if __name__ == "__main__":
    unittest.main()
