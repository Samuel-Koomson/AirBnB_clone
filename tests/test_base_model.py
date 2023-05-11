#!/usr/bin/python3
""" unittests for models/base_model.py
class:-
        Initialize
"""
import models
import unittest
import datetime
import time
from models.base_model import BaseModel

class TestBaseModel_Initialize(unittest.TestCase):
    """Unittests for testing initializtion of the BaseModel class."""

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

class TestBaseModel_dict(unittest.TestCase):
     """Unittests for testing dict of the BaseModel class.""" 

     def test_to_dict_type(self):
        bm = BaseModel()
        self.assertTrue(dict, type(bm.to_dict())) 


     def test_to_dict_contains_correct_keys(self):
        bm = BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())

class TestBaseModel_save(unittest.TestCase):
     """Unittests for testing save of the BaseModel class."""