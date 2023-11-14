#!/usr/bin/python3
"""A module that tests the Square class"""

import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    A class to test the Square Class
    """
    def test_pep8_base(self):
        """
        Test that checks PEP8
        """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/square.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_getter(self):
        r1 = Square(9)
        self.assertEqual(r1.size, 9)

    def test_setter(self):
        r1 = Square(9)
        r1.size = 7
        self.assertEqual(r1.size, 7)
