#!/usr/bin/python3
"""Unittest for Base Class"""

import unittest
from models.base import Base


class TesBase(unittest.TestCase):
    """Tests"""

    def test_id_given(self):
        """Test00"""
        self.assertTrue(Base(999), self.id == 999)
        self.assertTrue(Base(0), self.id == 0)
        self.assertTrue(Base(-80), self.id == -80)

    def test_id_not_given(self):
        """Test01"""
        self.assertTrue(Base(), self.id == 1)
        self.assertTrue(Base(), self.id == 2)

    def test_private_attr_access(self):
        """Test02"""
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)
            print(Base.nb_objects)