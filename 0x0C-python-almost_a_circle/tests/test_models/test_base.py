#!/usr/bin/python3

"""
Unit test for models/base.py
"""

import unittest
import os
from models.base import Base


class BaseTest(unittest.TestCase):
    """Tests for base class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_class_docstring(self):
        """Tests for the Base class docstring"""
        self.assertTrue(len(Base.__doc__) >= 1)

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

    """def test_load_from_files(self):
        os.remove("Base.json")
        base_list = Base.load_from_file()
        self.assertEqual(base_list, [])"""

if __name__ == '__main__':
    unittest.main()
