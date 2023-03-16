#!/usr/bin/python3
"""
module: test_state
resources: class TestState, unittest module
"""
import unittest
from models.state import State

class TestState(unittest.TestCase):
    def setUp(self):
        self.state_1 = State()

    def test_name(self):
        self.assertEqual(State.name, "")
        self.assertEqual(self.state_1.name, "")
        self.state_1.name = "Kenya"
        self.assertEqual(State.name, "")
        self.assertEqual(self.state_1.name, "Kenya")


if __name__ == "__main__":
    unittest.main()
