#!/usr/bin/python3

import unittest
from models.square import Square
import sys
from io import StringIO
import os


class TestSquare(unittest.TestCase):
    """test square class"""

    def test_instanciate_works(self):
        s1 = Square(2)
        s2 = Square(1, 2)
        s3 = Square(1, 2, 3)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s2.size, 1)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s3.size, 1)
        self.assertEqual(s3.x, 2)
        self.assertEqual(s3.y, 3)
        
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

    def test_to_dictionary(self):
        s = Square(1, 2, 3, 4)
        dict = { 'size': 1, 'x': 2, 'y': 3, 'id': 4 }
        self.assertEqual(s.to_dictionary(), dict)

    def test_update_args(self):
        s = Square(1, 1, 1, 1)
        s.update()
        self.assertEqual("[Square] (1) 1/1 - 1", str(s))
        s.update(2)
        self.assertEqual("[Square] (2) 1/1 - 1", str(s))
        s.update(3, 3)
        self.assertEqual("[Square] (3) 1/1 - 3", str(s))
        s.update(4, 4, 4)
        self.assertEqual("[Square] (4) 4/1 - 4", str(s))
        s.update(5, 5, 5, 5)
        self.assertEqual("[Square] (5) 5/5 - 5", str(s))

    def test_update_kwargs(self):
        s = Square(1, 1, 1, 1)
        s.update(id=2)
        self.assertEqual("[Square] (2) 1/1 - 1", str(s))
        s.update(id=3, size=3)
        self.assertEqual("[Square] (3) 1/1 - 3", str(s))
        s.update(id=4, size=4, x=4)
        self.assertEqual("[Square] (4) 4/1 - 4", str(s))
        s.update(id=5, size=5, x=5, y=5)
        self.assertEqual("[Square] (5) 5/5 - 5", str(s))

    def test_create(self):
        dict = {"x": 3, "y": 4, "id": 89, "size": 1}
        s = Square.create(**dict)
        self.assertEqual(str(s), "[Square] (89) 3/4 - 1")

    def test_save_to_file(self):
        try:
            os.remove("Square.json")
        except:
            pass

        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Square.json")
        except:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Square.json")
        except:
            pass

        Square.save_to_file([Square(1, 2, id=13)])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[{"id": 13, "size": 1, "x": 2, "y": 0}]')

    def test_load_from_file(self):
        try:
            os.remove("Square.json")
        except:
            pass
        self.assertEqual(Square.load_from_file(), [])

if __name__ == "__main__":
    unittest.main()
