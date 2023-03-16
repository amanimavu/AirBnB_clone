#!/usr/bin/python3
"""
module: test_user
resources: unittest module, TestUser class, User class
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    This class contains test cases that are used to
    test the User model
    """
    def setUp(self):
        """
        sets up things that are going to be needed
        for each test case
        """
        self.user_1 = User()

    def test_email(self):
        self.assertEqual(User.email, "")
        self.assertEqual(self.user_1.email, "")
        self.user_1.email = "amanimavu@gmail.com"
        self.assertEqual(User.email, "")
        self.assertEqual(self.user_1.email, "amanimavu@gmail.com")

    def test_password(self):
        self.assertEqual(User.password, "")
        self.assertEqual(self.user_1.password, "")
        self.user_1.password = "@abc#123"
        self.assertEqual(User.email, "")
        self.assertEqual(self.user_1.password, "@abc#123")

    def test_first_name(self):
        self.assertEqual(User.first_name, "")
        self.assertEqual(self.user_1.first_name, "")
        self.user_1.first_name = "Amani"
        self.assertEqual(User.first_name, "")
        self.assertEqual(self.user_1.first_name, "Amani")

    def test_email(self):
        self.assertEqual(User.last_name, "")
        self.assertEqual(self.user_1.last_name, "")
        self.user_1.last_name = "Mkongo"
        self.assertEqual(User.email, "")
        self.assertEqual(self.user_1.last_name, "Mkongo")


if __name__ == "__main__":
    unittest.main()
