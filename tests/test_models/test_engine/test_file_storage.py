#!/usr/bin/python3
"""
This test file is used to test the
file_storage module
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import unittest
import os


class TestFileStorage(unittest.TestCase):
    """
    The this class contains tests for the
    FileStorage class
    """
    def setUp(self):
        """
        Initializes everything required to test
        attributes of the class FileStorage
        """
        self.storage = FileStorage()
        self.base = BaseModel()
        FileStorage._FileStorage__objects = {}

    def test_file_path(self):
        """
        Tests whether we have specified the file
        used for storage
        """
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_objects(self):
        """
        Test the private class variable __objects
        which is used to save objects when the
        program is running
        """
        self.assertEqual(len(self.storage._FileStorage__objects), 0)
        self.storage.new(self.base)
        self.assertEqual(len(self.storage._FileStorage__objects), 1)
        object_key = "BaseModel.{}".format(self.base.id)
        self.assertEqual(
                type(self.storage._FileStorage__objects[object_key]),
                BaseModel
                )

    def test_save(self):
        """
        Tests the save method which is used to
        make the program persistent. Checks if
        the save method modifies file.json
        """
        self.storage.reload()
        path = "file.json"
        file_stat_1 = os.stat(path)
        self.storage.new(self.base)
        self.storage.save()
        file_stat_2 = os.stat(path)
        self.assertTrue(os.path.exists(path))
        self.assertFalse(file_stat_1 == file_stat_2)

    def test_update(self):
        self.assertEqual(len(self.storage._FileStorage__objects), 0)
        self.storage.reload()
        self.assertTrue(len(self.storage._FileStorage__objects) > 0)


if __name__ == "__main__":
    unittest.main()
