#!/usr/bin/python3
"""
A module that test differents behaviors
of the Rectangle class
"""
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    A class to test the Rectangle Class
    """
    def test_pep8_base(self):
        """
        Test that checks PEP8
        """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/rectangle.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_rectangle_subclass(self):
        """
        Test if Rectangle class correctly inherits from
        Base class
        """
        self.assertTrue(issubclass(Rectangle, Base))

    def test_parameters(self):
        """
        Parameters to test Rectangle class
        """
        r1 = Rectangle(1, 20)
        r2 = Rectangle(24, 9)
        r3 = Rectangle(6, 11, 0, 0, 9)

        self.assertEqual(r1.id, 4)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.id, 5)
        self.assertEqual(r2.width, 24)
        self.assertEqual(r2.height, 9)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r3.id, 9
        self.assertEqual(r3.width, 6)
        self.assertEqual(r3.height, 11)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

        with self.assertRaises(TypeError):
            r4 = Rectangle()
