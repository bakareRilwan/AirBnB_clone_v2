#!/usr/bin/python3
"""Instantiates a storage object.
-> If the environmental variable 'HBNB_TYPE_STORAGE' is set to 'db',
   instantiates a database storage engine (DBStorage).
-> Otherwise, instantiates a file storage engine (FileStorage).
"""
import os
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage


env = os.getenv("HBNB_TYPE_STORAGE")

if env == "db":
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
