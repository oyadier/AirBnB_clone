#!/usr/bin/python3
"""Initializer that passes storage function"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
