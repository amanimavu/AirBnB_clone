#!/usr/bin/python3
"""
module: test_base_model
resources:
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """
    This class contains tests for different
    methods found in the BaseModel class
    """
    def setUp(self):
        self.base_1 = BaseModel()

    def test_init(self):
        """
        This is a test case that test the initialization
        of the BaseModel object
        """
        self.assertEqual(type(self.base_1.created_at), datetime)
        self.assertEqual(type(self.base_1.updated_at), datetime)
        self.assertEqual(type(self.base_1.id), str)
        self.assertEqual(self.base_1.created_at, self.base_1.updated_at)

    @unittest.expectedFailure
    def test_save(self):
        """
        This test validates that the datetime for creation
        and update are different when the object is saved
        """
        self.base_1.save()
        self.assertEqual(self.base_1.created_at, self.base_1.updated_at)

    def test_to_dict(self):
        """
        This method test the to_dict() method of the base
        model. It checks whether a json like dictionary
        is returned by the method to_dict()
        """
        dictionary = self.base_1.to_dict()
        self.assertEqual(type(dictionary), dict)
        for value in dictionary.values():
            self.assertEqual(type(value), str)

        self.assertEqual(dictionary["__class__"], "BaseModel")
        # even after using to_dict() method the object type
        # for created_at and updated_at remain as datetime
        # they must not be converted to str
        self.assertEqual(type(self.base_1.created_at), datetime)
        self.assertEqual(type(self.base_1.updated_at), datetime)


if __name__ == "__main__":
    unittest.main()
