#!/usr/bin/python3
"""
module: test_review
resources: unittest module, TestReview class,
Place, User and Review class
"""
import unittest
from models.place import Place
from models.user import User
from models.review import Review


class TestReview(unittest.TestCase):
    def setUp(self):
        self.review_1 = Review()
        self.user_1 = User()
        self.place_1 = Place()

    def test_text(self):
        self.assertEqual(self.review_1.text, "")
        self.assertEqual(Review.text, "")
        self.review_1.text = "I had a great experience"
        self.assertEqual(self.review_1.text, "I had a great experience")
        self.assertEqual(Review.text, "")

    def test_place_id(self):
        self.assertEqual(self.review_1.place_id, "")
        self.assertEqual(Review.place_id, "")
        place_1 = Place()
        self.review_1.place_id = place_1.id
        self.assertEqual(self.review_1.place_id, place_1.id)
        self.assertEqual(Review.place_id, "")

    def test_user_id(self):
        self.assertEqual(self.review_1.user_id, "")
        self.assertEqual(Review.user_id, "")
        user_1 = User()
        self.review_1.user_id = user_1.id
        self.assertEqual(self.review_1.user_id, user_1.id)
        self.assertEqual(Review.user_id, "")


if __name__ == "__main__":
    unittest.main()
