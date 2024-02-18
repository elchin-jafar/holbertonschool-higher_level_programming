#!/usr/bin/python3

import unittest

from models.base import Base


class TestBase(unittest.TestCase):
    """test base class from models module"""

    def test_id_exists(self):
        b1 = Base()
        self.assertEqual(b1.id, 3)

    def test_id_auto_increment(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_manual_id(self):
        b1 = Base(89)
        self.assertEqual(b1.id, 89)

    def test_negative_id(self):
        b1 = Base(-1)
        self.assertEqual(b1.id, -1)

    def test_to_json_string_none(self):
        res = Base.to_json_string(None)
        self.assertEqual('[]', res)

    def test_to_json_string_empty_list(self):
        res = Base.to_json_string([])
        self.assertEqual('[]', res)

    def test_to_json_string(self):
        res = Base.to_json_string([ { 'id': 22 } ])
        self.assertTrue(res)
        self.assertEqual(str, type(res))

if __name__ == '__main__':
    unittest.main()
