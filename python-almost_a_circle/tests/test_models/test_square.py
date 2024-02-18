#!/usr/bin/python3

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """test square class"""

    def test_instanciate_works(self):
        s = Square(2)
        self.assertEqual(s.size, 2)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        s1 = Square(10)
        s2 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_args(self):
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        s1 = Square(10, 2, 2)
        s2 = Square(2, 2, 10)
        self.assertEqual(s1.id, s2.id - 1)
