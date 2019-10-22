#!/usr/bin/python3

"""
Unit test for models/rectangle.py
"""

import sys
import os
import io
import contextlib
import unittest
from models.rectangle import Rectangle
from models.base import Base


class RectangleTest(unittest.TestCase):
    """Tests for rectangle class."""

    def test_class_docstring(self):
        """Tests for the presence of a class docstring"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        if os.path.exists("Base.json"):
            os.remove("Base.json")
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_isinstance(self):
        r = Rectangle(1, 2)
        self.assertEqual(isinstance(r, Base), True)

    def test_float_nan(self):
        with self.assertRaises(TypeError) as x:
            r = Rectangle(float("nan"), 1)
        self.assertEqual(
            "width must be an integer",
            str(x.exception))

    def test_float_nan(self):
        with self.assertRaises(TypeError) as x:
            r = Rectangle(float("inf"), 1)
        self.assertEqual(
            "width must be an integer",
            str(x.exception))

    def test_one_arg(self):
        with self.assertRaises(TypeError) as e:
            r = Rectangle(5)
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'height'",
            str(e.exception))

    def test_two_args(self):
        r = Rectangle(10, 2)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_three_args(self):
        r = Rectangle(98, 12, 64)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 98)
        self.assertEqual(r.height, 12)
        self.assertEqual(r.x, 64)
        self.assertEqual(r.y, 0)

    def test_four_args(self):
        r = Rectangle(4, 51, 96, 88)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 51)
        self.assertEqual(r.x, 96)
        self.assertEqual(r.y, 88)

    def test_five_args(self):
        r = Rectangle(5, 66, 151, 44, 822)
        self.assertEqual(r.id, 822)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 66)
        self.assertEqual(r.x, 151)
        self.assertEqual(r.y, 44)

    def test_private_attributes(self):
        r = Rectangle(11, 6, 87, 6, 91)
        d = {"_Rectangle__width": 11, "_Rectangle__height": 6,
             "_Rectangle__x": 87, "_Rectangle__y": 6, "id": 91}
        self.assertEqual(r.__dict__, d)

    def test_none(self):
        with self.assertRaises(TypeError) as x:
            r = Rectangle(None)
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'height'",
            str(x.exception))

    def test_no_args(self):
        with self.assertRaises(TypeError) as x:
            r = Rectangle()
        self.assertEqual(
            "__init__() missing 2 required positional arguments:" +
            " 'width' and 'height'",
            str(x.exception))

    def test_string_test(self):
        with self.assertRaises(TypeError) as x:
            r = Rectangle(10, "2")
        self.assertEqual(
            "height must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Rectangle("10", 2)
        self.assertEqual(
            "width must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r8 = Rectangle(10, 2, "3")
        self.assertEqual(
            "x must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Rectangle(10, 2, 0, "lol")
        self.assertEqual(
            "y must be an integer",
            str(x.exception))

    def test_float_test(self):
        with self.assertRaises(TypeError) as x:
            r = Rectangle(10, 2.1)
        self.assertEqual(
            "height must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Rectangle(9.0, 2)
        self.assertEqual(
            "width must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Rectangle(10, 2, 3.2131)
        self.assertEqual(
            "x must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Rectangle(10, 2, 0, 1662.1)
        self.assertEqual(
            "y must be an integer",
            str(x.exception))

    def test_negative_ints(self):
        with self.assertRaises(ValueError) as x:
            r = Rectangle(1, -2)
        self.assertEqual(
            "height must be > 0",
            str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Rectangle(-1, -2)
        self.assertEqual(
            "width must be > 0",
            str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Rectangle(1, 2, -1)
        self.assertEqual(
            "x must be >= 0",
            str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Rectangle(1, 2, 5, -1)
        self.assertEqual(
            "y must be >= 0",
            str(x.exception))

    def test_zero(self):
        with self.assertRaises(ValueError) as x:
            r = Rectangle(6, 0)
        self.assertEqual(
            "height must be > 0",
            str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Rectangle(0, 2)
        self.assertEqual(
            "width must be > 0",
            str(x.exception))
        r = Rectangle(1, 2, 0, 0)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_area(self):
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)
        r = Rectangle(1, 20, 1)
        self.assertEqual(r.area(), 20)
        r = Rectangle(4, 5, 6, 2)
        self.assertEqual(r.area(), 20)
        r = Rectangle(9, 7, 4, 6, 12)
        self.assertEqual(r.area(), 63)

    def test_display(self):
        r = Rectangle(4, 6)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        s = f.getvalue()
        four_by_six = "####\n####\n####\n####\n####\n####\n"
        self.assertEqual(s, four_by_six)
        r = Rectangle(2, 4)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        s = f.getvalue()
        two_by_four = "##\n##\n##\n##\n"
        self.assertEqual(s, two_by_four)
        r = Rectangle(1, 1)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        s = f.getvalue()
        one_by_one = "#\n"
        self.assertEqual(s, one_by_one)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r.__str__(), "[Rectangle] (12) 2/1 - 4/6")
        r = Rectangle(5, 5, 1, 1)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 1/1 - 5/5")
        r = Rectangle(1, 1, 0)
        self.assertEqual(r.__str__(), "[Rectangle] (2) 0/0 - 1/1")
        r = Rectangle(1, 1)
        self.assertEqual(r.__str__(), "[Rectangle] (3) 0/0 - 1/1")

    def test_display_with_coords(self):
        r = Rectangle(2, 3, 2, 2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        s = f.getvalue()
        output = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(s, output)
        r = Rectangle(3, 2, 0, 0)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        s = f.getvalue()
        output = "###\n###\n"
        self.assertEqual(s, output)

    def test_update_args(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        r.update(90, 2)
        self.assertEqual(r.__str__(), "[Rectangle] (90) 10/10 - 2/10")
        r.update(91, 3, 4)
        self.assertEqual(r.__str__(), "[Rectangle] (91) 10/10 - 3/4")
        r.update(92, 6, 7, 8)
        self.assertEqual(r.__str__(), "[Rectangle] (92) 8/10 - 6/7")
        r.update(93, 9, 10, 11, 12)
        self.assertEqual(r.__str__(), "[Rectangle] (93) 11/12 - 9/10")
        r = Rectangle(1, 1)
        r.update(1, 2, 3, 4, 5)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 4/5 - 2/3")

    def test_update_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(height=1)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 10/10 - 10/1")
        r.update(width=1, x=2)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 2/10 - 1/1")
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 3/1 - 2/1")

    def test_args_and_kwargs(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(99, height=66)
        self.assertEqual(r.__str__(), "[Rectangle] (99) 3/4 - 1/2")

    def test_invalid_kwargs(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(weight=25)
        self.assertEqual(hasattr(r, 'weight'), False)

    def test_empty_update(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update()
        self.assertEqual(r.__str__(), "[Rectangle] (5) 3/4 - 1/2")

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9)
        r_d = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(r.to_dictionary(), r_d)
        self.assertEqual(r.to_dictionary() is r_d, False)
        r = Rectangle(9, 4, 15)
        r_d = {'width': 9, 'height': 4, 'x': 15, 'id': 2, 'y': 0}
        self.assertEqual(r.to_dictionary(), r_d)
        self.assertEqual(r.to_dictionary() is r_d, False)
        r = Rectangle(62, 414)
        r_d = {'width': 62, 'height': 414, 'x': 0, 'id': 3, 'y': 0}
        self.assertEqual(r.to_dictionary(), r_d)
        self.assertEqual(r.to_dictionary() is r_d, False)
        r = Rectangle(1, 2, 3, 4, 5)
        r_d = {'width': 1, 'height': 2, 'x': 3, 'id': 5, 'y': 4}
        self.assertEqual(r.to_dictionary(), r_d)
        self.assertEqual(r.to_dictionary() is r_d, False)

    def test_to_json_string(self):
        r = Rectangle(10, 7, 2, 8)
        d = r.to_dictionary()
        json_d = Base.to_json_string([d])
        self.assertEqual(type(json_d), str)
        self.assertEqual(
            d, {'height': 7, 'id': 1, 'width': 10, 'x': 2, 'y': 8})

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        res = '[{"x": 2, "y": 8, "id": 2, "height": 7, "width": 10},' + \
            ' {"x": 0, "y": 0, "id": 3, "height": 4, "width": 2}]'
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), len(res))

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError) as e:
            Rectangle.save_to_file()
        self.assertEqual("save_to_file() missing 1 required positional" +
                         " argument: 'list_objs'",
                         str(e.exception))

    def test_from_json_string(self):
        list_input = [{'id': 89, 'width': 10, 'height': 4},
                      {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        l = [{'height': 4, 'width': 10, 'id': 89},
             {'height': 7, 'width': 1, 'id': 7}]
        self.assertEqual(list_output, l)

    def test_create(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual((r1 == r2), False)
        self.assertEqual((r1 is r2), False)

    def test_create_none(self):
        r = Rectangle(1, 1)
        r_dictionary = r.to_dictionary()
        with self.assertRaises(TypeError) as e:
            r = Rectangle.create(None)
        self.assertEqual(
            "create() takes 1 positional argument but 2 were given", str(
                e.exception))

    def test_create_string(self):
        r = Rectangle(1, 1)
        r_dictionary = r.to_dictionary()
        with self.assertRaises(TypeError) as e:
            r = Rectangle.create("hello")
        self.assertEqual(
            "create() takes 1 positional argument but 2 were given", str(
                e.exception))

    def test_create_list(self):
        r = Rectangle(1, 1)
        r_dictionary = r.to_dictionary()
        with self.assertRaises(TypeError) as e:
            r = Rectangle.create([1, 2, 3])
        self.assertEqual(
            "create() takes 1 positional argument but 2 were given", str(
                e.exception))

    def test_create_int(self):
        r = Rectangle(1, 1)
        r_dictionary = r.to_dictionary()
        with self.assertRaises(TypeError) as e:
            r = Rectangle.create(1)
        self.assertEqual(
            "create() takes 1 positional argument but 2 were given", str(
                e.exception))

    def test_create_float(self):
        r = Rectangle(1, 1)
        r_dictionary = r.to_dictionary()
        with self.assertRaises(TypeError) as e:
            r = Rectangle.create(1.0)
        self.assertEqual(
            "create() takes 1 positional argument but 2 were given", str(
                e.exception))

    def test_create_set(self):
        r = Rectangle(1, 1)
        r_dictionary = r.to_dictionary()
        with self.assertRaises(TypeError) as e:
            r = Rectangle.create({1, 2, 3})
        self.assertEqual(
            "create() takes 1 positional argument but 2 were given", str(
                e.exception))

    def test_create_invalid_key(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(volume=1)
        self.assertEqual(r1.__dict__ == r2.__dict__, False)

    def test_load_from_files(self):
        rect_list = Rectangle.load_from_file()
        self.assertEqual(rect_list, [])

    def test_load_from_files(self):
        with self.assertRaises(TypeError) as e:
            rect_list = Rectangle.load_from_file("Rectangle.json")
        self.assertEqual(
            "load_from_file() takes 1 positional argument but 2 were given",
            str(e.exception))

    def test_save_to_csv(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9)
        r3 = Rectangle(10, 11, 12)
        r4 = Rectangle(13, 14)
        list_rectangles_input = [r1, r2, r3, r4]
        Rectangle.save_to_file_csv(list_rectangles_input)
        with open("Rectangle.csv", "r") as f:
            data = f.readlines()
        self.assertEqual(data[0], '5,1,2,3,4\n')
        self.assertEqual(data[1], '1,6,7,8,9\n')
        self.assertEqual(data[2], '2,10,11,12,0\n')
        self.assertEqual(data[3], '3,13,14,0,0\n')

    def test_save_to_file_None(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[]')

    def test_save_to_file_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[]')
        empty = []
        Rectangle.save_to_file(empty)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[]')

    def test_save_to_file_two_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([], 6)

if __name__ == '__main__':
    unittest.main()
