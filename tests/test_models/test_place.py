#!/usr/bin/python3
"""
module: test_place
resources: unittest module, Place class,
City class, User class and TestPlace class
"""
import unittest
from models.place import Place
from models.city import City
from models.user import User

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place_1 = Place()

    def test_city_id(self):
        self.assertEqual(Place.city_id, "")
        self.assertEqual(self.place_1.city_id, "")
        city_1 = City()
        self.place_1.city_id = city_1.id
        self.assertEqual(self.place_1.city_id, city_1.id)
        self.assertEqual(Place.city_id, "")

    def test_user_id(self):
        self.assertEqual(Place.city_id, "")
        self.assertEqual(self.place_1.user_id, "")
        user_1 = User()
        self.place_1.user_id = user_1.id
        self.assertEqual(self.place_1.user_id, user_1.id)
        self.assertEqual(Place.user_id, "")

    def test_name(self):
        self.assertEqual(Place.city_id, "")
        self.assertEqual(self.place_1.city_id, "")
        self.place_1.name = "Lavington"
        self.assertEqual(self.place_1.name, "Lavington")
        self.assertEqual(Place.name, "")

    def test_description(self):
        self.assertEqual(Place.city_id, "")
        self.assertEqual(self.place_1.city_id, "")
        self.place_1.description = "A nice place"
        self.assertEqual(self.place_1.description, "A nice place")
        self.assertEqual(Place.city_id, "")


if __name__ == "__main__":
    unittest.main()
