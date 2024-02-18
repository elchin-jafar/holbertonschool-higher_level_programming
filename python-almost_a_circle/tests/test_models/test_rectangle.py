#!/usr/bin/python3

import unittest
import sys
from io import StringIO
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """test rectangle class"""

    def test_instanciate_works(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_rectangle_typeError(self):
        with self.assertRaises(TypeError):
            Rectangle('1', 2)
        with self.assertRaises(TypeError):
            Rectangle(1, '2')
        with self.assertRaises(TypeError):
            Rectangle(1, 2, '3')
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, '4')

    def test_rectangle_valueError(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(2, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)
        
    def test_rectangle_work_on_every_argument_pass(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)

    def test_area(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)

    def test_str(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.__str__(), "[Rectangle] (5) 3/4 - 1/2")

    def test_display(self):
        r = Rectangle(2, 2, 1, 1, 1)
        captured_output = StringIO()
        sys.stdout = captured_output
        r.display()
        printed_output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
        self.assertEqual(printed_output, "\n ##\n ##\n")

    def test_display_without_y(self):
        r = Rectangle(2, 2, 1)
        captured_output = StringIO()
        sys.stdout = captured_output
        r.display()
        printed_output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
        self.assertEqual(printed_output, " ##\n ##\n")

    def test_display_without_x_y(self):
        r = Rectangle(2, 2)
        captured_output = StringIO()
        sys.stdout = captured_output

        r.display()

        printed_output = captured_output.getvalue()

        sys.stdout = sys.__stdout__
        self.assertEqual(printed_output, "##\n##\n")
