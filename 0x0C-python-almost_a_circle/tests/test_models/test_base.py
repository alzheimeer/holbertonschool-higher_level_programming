#!/usr/bin/python3
"""Unit test base"""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class BaseTest(unittest.TestCase):
    """Tests for base class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_class_docstring(self):
        """Tests for the Base class docstring"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_A_nb_objects_private(self):
        '''Tests if nb_objects is private class attribute.'''
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_B_nb_objects_initialized(self):
        '''Tests if nb_objects initializes to zero.'''
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_C_instantiation(self):
        '''Tests Base() instantiation.'''
        b = Base()
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")
        self.assertEqual(b.__dict__, {"id": 1})
        self.assertEqual(b.id, 1)

    def test_D_constructor(self):
        '''Tests constructor signature.'''
        with self.assertRaises(TypeError) as e:
            Base.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_D_constructor_args_2(self):
        '''Tests constructor signature with 2 notself args.'''
        with self.assertRaises(TypeError) as e:
            Base.__init__(self, 1, 2)
        msg = "__init__() takes from 1 to 2 positional arguments but 3 \
were given"
        self.assertEqual(str(e.exception), msg)

    def test_E_consecutive_ids(self):
        '''Tests consecutive ids.'''
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_F_id_synced(self):
        '''Tests sync between class and instance id.'''
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    def test_F_id_synced_more(self):
        '''Tests sync between class and instance id.'''
        b = Base()
        b = Base("Foo")
        b = Base(98)
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    def test_G_custom_id_int(self):
        '''Tests custom int id.'''
        i = 98
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_G_custom_id_str(self):
        '''Tests custom int id.'''
        i = "FooBar"
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_G_id_keyword(self):
        '''Tests id passed as keyword arg.'''
        i = 421
        b = Base(id=i)
        self.assertEqual(b.id, i)

    def test_correct_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_custom_id(self):
        b = Base(98)
        self.assertEqual(b.id, 98)

    def test_correct_id_after_custom(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_string_input(self):
        b = Base("hello")
        self.assertEqual(b.id, "hello")

    def test_none_input(self):
        b = Base(None)
        self.assertEqual(b.id, 1)

    def test_zero_input(self):
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_negative_input(self):
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_list_input(self):
        b = Base([1, 2, 3])
        self.assertEqual(b.id, [1, 2, 3])

    def test_class_type(self):
        b = Base()
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")
        self.assertEqual(b.__dict__, {"id": 1})

    def test_private_id(self):
        b = Base(1)
        with self.assertRaises(Exception) as e:
            print(b.nb__objects)
        self.assertEqual(
            "'Base' object has no attribute 'nb__objects'",
            str(e.exception))

    def test_json_none(self):
        res = Base.to_json_string(None)
        self.assertEqual(res, "[]")

    def test_json_empty_list(self):
        res = Base.to_json_string([])
        self.assertEqual(res, "[]")

    def test_json_no_args(self):
        with self.assertRaises(TypeError) as e:
            res = Base.to_json_string()
        self.assertEqual("to_json_string() missing 1 required positional " +
                         "argument: 'list_dictionaries'", str(e.exception))

    def test_json_list_of_multiple_dicts(self):
        res = Base.to_json_string([{"a": 1}, {"b": 2}])
        self.assertEqual(type(res), str)

    def test_json_list_of_empty_dict(self):
        res = Base.to_json_string([{}])
        self.assertEqual(res, "[{}]")

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError) as e:
            res = Base.save_to_file()
        self.assertEqual("save_to_file() missing 1 required positional " +
                         "argument: 'list_objs'", str(e.exception))

    def test_save_None_to_file(self):
        Base.save_to_file(None)
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_empty_list_to_file(self):
        Base.save_to_file([])
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_from_json_string_None(self):
        list_output = Base.from_json_string(None)
        self.assertEqual(list_output, [])

    def test_from_json_string_empty_string(self):
        list_output = Base.from_json_string("")
        self.assertEqual(list_output, [])

    def test_from_json_string_no_arg(self):
        with self.assertRaises(TypeError) as e:
            list_output = Base.from_json_string()
        self.assertEqual("from_json_string() missing 1 required positional " +
                         "argument: 'json_string'",
                         str(e.exception))

    def test_from_json_string_non_dicts(self):
        list_input = [{}, {}]
        json_list_input = Base.to_json_string(list_input)
        list_output = Base.from_json_string(json_list_input)
        self.assertEqual(list_output, [{}, {}])

    def test_J_create(self):
        '''Tests create() method.'''
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_K_load_from_file(self):
        '''Tests load_from_file() method.'''
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_in = [r1, r2]
        Rectangle.save_to_file(list_in)
        list_out = Rectangle.load_from_file()
        self.assertNotEqual(id(list_in[0]), id(list_out[0]))
        self.assertEqual(str(list_in[0]), str(list_out[0]))
        self.assertNotEqual(id(list_in[1]), id(list_out[1]))
        self.assertEqual(str(list_in[1]), str(list_out[1]))

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_in = [s1, s2]
        Square.save_to_file(list_in)
        list_out = Square.load_from_file()
        self.assertNotEqual(id(list_in[0]), id(list_out[0]))
        self.assertEqual(str(list_in[0]), str(list_out[0]))
        self.assertNotEqual(id(list_in[1]), id(list_out[1]))
        self.assertEqual(str(list_in[1]), str(list_out[1]))


if __name__ == '__main__':
    unittest.main()
