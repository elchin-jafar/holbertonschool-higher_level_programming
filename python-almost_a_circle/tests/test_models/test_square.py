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

    def test_square_typeError(self):
        with self.assertRaises(TypeError):
            Square('1')
        with self.assertRaises(TypeError):
            Square(1, '2')
        with self.assertRaises(TypeError):
            Square(1, 2, '3')

    def test_square_valueError(self):
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_zero_size(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.__str__(), "[Square] (4) 2/3 - 1")
