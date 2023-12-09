#!/usr/bin/python3
"""All test case for the user class"""
from models.user import User
from models.base_model import BaseModel
import unittest


class TestUser(unittest.TestCase):
    """User possible test cases"""

    def test_isInstance(self):
        """Checks if user is BaseModel"""
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_hasAttribute(self):
        user = User()
        self.assertTrue("first_name" in user.__dir__())
