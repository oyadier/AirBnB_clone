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
        """Test if is an attribute"""
        user = User()
        self.assertTrue("first_name" in user.__dir__())
        self.assertTrue("last_name" in user.__dir__())
        self.assertTrue("email" in user.__dir__())
        self.assertTrue("password" in user.__dir__())

    def test_attribute_type1(self):
        """test string type"""
        user = User()
        name = getattr(user, "email")
        self.assertIsInstance(name, str)

    def test_attribute_type2(self):
        """test string type"""
        user = User()
        name = getattr(user, "first_name")
        self.assertIsInstance(name, str)

    def test_attribute_type3(self):
        """test string type"""
        user = User()
        name = getattr(user, "last_name")
        self.assertIsInstance(name, str)

    def test_attribute_type4(self):
        """test string type"""
        user = User()
        name = getattr(user, "password")
        self.assertIsInstance(name, str)

    def test_has_no_attribute(self):
        """Test for not attribute"""
        user = User()
        self.assertFalse("not_exit" in user.__dir__())
