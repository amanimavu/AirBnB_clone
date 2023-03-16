#!/usr/bin/python3
"""
This module contains tests for the class
City
"""
import unittest
from models.city import City
from models.state import State

class TestCity(unittest.TestCase):
    def setUp(self):
        """
        prepares things that are necessary before each
        test case runs
        """
        self.city_1 = City()
        self.state_1 = State()

    def test_state_id(self):
        self.assertEqual(self.city_1.state_id, "")
        self.city_1.state_id = self.state_1.id
        self.assertEqual(self.city_1.state_id, self.state_1.id)
        self.assertEqual(City.state_id, "")

    def test_name(self):
        self.assertEqual(self.city_1.name, "")
        self.city_1.name = "Nairobi"
        self.assertEqual(self.city_1.name, "Nairobi")
        self.assertEqual(City.name, "")


if __name__ == "__main__":
    unittest.main()
