import unittest
from base import Base


class TestBase(unittest.TestCase):
    def test_base(self):
        b = Base()
        self.assertIsInstance(b, Base)
        self.assertEqual(b.id, 1)

if __name__ == "__main__":
    unittest.main()
