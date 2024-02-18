import unittest

from models.base import Base


class TestBase(unittest.TestCase):
    """test base class from models module"""

    def test_id_exists(self):
        b1 = Base()
        self.assertTrue(b1.id)
