#!/usr/bin/python
"""
module: test_base_model
resources: unittest module and
"""
from models.base_model import BaseModel

import unittest

class TestBaseModel(unittest.TestCase):
    """

    """
    def set_up(self):
        self.base = BaseModel()

    def test_str(self):
        string = "[BaseModel]", \
        "(fbe5f327-c8ec-4665-a162-c685bdef3b4a)",\
        "{'id': 'fbe5f327-c8ec-4665-a162-c685bdef3b4a', 'created_at':",\
            "datetime.datetime(2023, 3, 6, 15, 36, 14, 361696),",\
            "'updated_at': datetime.datetime(2023, 3, 6, 15, 36, 14, 361696),",\
            "'name': 'My_First_Model', 'my_number': 89}"
        self.assertEqual(str(self.base), string)

if __name__ == "__main__":
    unittest.main()
