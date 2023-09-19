#!/usr/bin/python3
from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    def test_rect(self):
        b = Rectangle(4, 6)
        self.assertIsInstance(b, Rectangle)
        self.assertEqual(b.id, 1)

if __name__ == "__main__":
    unittest.main()
