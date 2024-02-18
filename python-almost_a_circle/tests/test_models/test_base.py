import unittest

from models.base import Base


class TestBase(unittest.TestCase):
    """test base class from models module"""

    def test_id_exists(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

if __name__ == '__main__':
    unittest.main()
