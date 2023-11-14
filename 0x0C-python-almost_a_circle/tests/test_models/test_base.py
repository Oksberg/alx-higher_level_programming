#!/usr/bin/python3
"""
A module that test differents behaviors
of the Base class
"""
import unittest
import pep8
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    A class to test the Base Class
    """
    def test_pep8_base(self):
        """
        Test that checks PEP8
        """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/base.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_id_as_positive(self):
        """
        Test for a positive Base Class id
        """
        base_instance = Base(24)
        self.assertEqual(base_instance.id, 24)
        base_instance = Base(201)
        self.assertEqual(base_instance.id, 201)

    def test_id_as_negative(self):
        """
        Test for a negative Base Class id
        """
        base_instance = Base(-90)
        self.assertEqual(base_instance.id, -90)
        base_instance = Base(-9)
        self.assertEqual(base_instance.id, -9)

    def test_id_as_none(self):
        """
        Test for a None Base Class id
        """
        base_instance = Base()
        self.assertEqual(base_instance.id, 1)
        base_instance = Base(None)
        self.assertEqual(base_instance.id, 2)
