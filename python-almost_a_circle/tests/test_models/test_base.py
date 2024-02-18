import unittest

from models.base import Base

class TestBase(unittest.TestCase):
    """test base class from models module"""

    def test_increment_id_on_init(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
