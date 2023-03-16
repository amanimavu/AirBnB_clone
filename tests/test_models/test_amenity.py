#!/usr/bin/python3
"""
module: test_amenity
resources: unittest module, Amenity class,
TestAmenity class
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity_1 = Amenity()

    def test_name(self):
        self.assertEqual(Amenity.name, "")
        self.assertEqual(self.amenity_1.name, "")
        self.amenity_1.name = "WiFi"
        self.assertEqual(self.amenity_1.name, "WiFi")
        self.assertEqual(Amenity.name, "")


if __name__ == "__main__":
    unittest.main()
