#!/usr/bin/python3

import unittest
import sys
from io import StringIO
from models.rectangle import Rectangle
import os


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

    def test_to_dictionary(self):
        r = Rectangle(1, 2, 3, 4, 5)
        dict = { 'width': 1, 'height': 2, 'x': 3, 'y': 4, 'id': 5 }
        self.assertEqual(r.to_dictionary(), dict)

    def test_update_args(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update()
        self.assertEqual("[Rectangle] (1) 1/1 - 1/1", str(r))
        r.update(2)
        self.assertEqual("[Rectangle] (2) 1/1 - 1/1", str(r))
        r.update(3, 3)
        self.assertEqual("[Rectangle] (3) 1/1 - 3/1", str(r))
        r.update(4, 4, 4)
        self.assertEqual("[Rectangle] (4) 1/1 - 4/4", str(r))
        r.update(5, 5, 5, 5)
        self.assertEqual("[Rectangle] (5) 5/1 - 5/5", str(r))
        r.update(6, 6, 6 ,6 ,6)
        self.assertEqual("[Rectangle] (6) 6/6 - 6/6", str(r))

    def test_update_kwargs(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(id=2)
        self.assertEqual("[Rectangle] (2) 1/1 - 1/1", str(r))
        r.update(id=3, width=3)
        self.assertEqual("[Rectangle] (3) 1/1 - 3/1", str(r))
        r.update(id=4, width=4, height=4)
        self.assertEqual("[Rectangle] (4) 1/1 - 4/4", str(r))
        r.update(id=5, width=5, height=5, x=5)
        self.assertEqual("[Rectangle] (5) 5/1 - 5/5", str(r))
        r.update(id=6, width=6, height=6, x=6, y=6)
        self.assertEqual("[Rectangle] (6) 6/6 - 6/6", str(r))

    def test_create(self):
        dict = {"height": 2, "width": 1, "x": 3, "y": 4, "id": 89}
        r = Rectangle.create(**dict)
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")

    def test_save_to_file(self):
        try:
            os.remove("Rectangle.json")
        except:
            pass
        
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        
        
        try:
            os.remove("Rectangle.json")
        except:
            pass
        
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        
        
        try:
            os.remove("Rectangle.json")
        except:
            pass
        
        Rectangle.save_to_file([Rectangle(1, 2, id=1)])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), '[{"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}]')

    def test_load_from_file(self):
        try:
            os.remove("Rectangle.json")
        except:
            pass
        self.assertEqual(Rectangle.load_from_file(), [])

if __name__ == "__main__":
    unittest.main()
