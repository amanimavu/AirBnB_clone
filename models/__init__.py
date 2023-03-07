#!/usr/bin/python3

"""
This file makes the package model importable.
Everytime the model package is imported,
reloading of the file storage happens.
"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
