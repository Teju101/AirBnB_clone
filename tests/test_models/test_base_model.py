#!/usr/bin/python3
"""Unittest for BaseModel class"""
import unittest
from models.base_model import BaseModel
import uuid
from datetime import datetime, time, date


class TestBaseModel(unittest.TestCase):
    """Test cases for class BaseModel"""


    def test_to_dict(self):
        """Test that to dict method works"""
        tmp = BaseModel().to_dict()
        self.assertTrue(isinstance(tmp, dict))
        self.assertTrue("updated_at" in tmp)
        self.assertTrue("created_at" in tmp)
        self.assertTrue("id" in tmp)
        self.assertTrue("__class__" in tmp)



if __name__ == "__main__":
    unittest.main()
