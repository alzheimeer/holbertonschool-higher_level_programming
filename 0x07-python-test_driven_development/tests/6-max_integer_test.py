#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Class for unittest of max_integer program"""

    def test_documentation(self):
        self.assertTrue(len(__import__("6-max_integer").__doc__) > 0)

        self.assertTrue(len(max_integer.__doc__) > 0)

    def test_positives(self):
        """Testing positive numbers"""

        pr = [1, 2, 3, 6]
        self.assertEqual(max_integer(pr), 6)

        pr = [1, 2, 6, 3]
        self.assertEqual(max_integer(pr), 6)

        pr = [4, 4, 4, 4]
        self.assertEqual(max_integer(pr), 4)

        pr = [1, 2, 6, 6]
        self.assertEqual(max_integer(pr), 6)

        pr = [1.1, 2.2, 3.3, 4.4]
        self.assertEqual(max_integer(pr), 4.4)


    def test_negatives(self):

        pr = [-2, 0, 2, 4]
        self.assertEqual(max_integer(pr), 4)

        pr = [-7, -6, -5, -4]
        self.assertEqual(max_integer(pr), -4)

    def test_none_and_zero(self):

        pr = []
        self.assertEqual(max_integer(pr), None)

        pr = [0, 0, 0, 0]
        self.assertEqual(max_integer(pr), 0)

        self.assertEqual(max_integer(), None)

    def test_not_list(self):

        pr = [1, 2, "mao", 4]
        self.assertRaises(TypeError)

        pr = [1, 2, [1, 2, 3], 4]
        self.assertRaises(TypeError)

        pr = [1, 2, (1, 2, 3), 4]
        self.assertRaises(TypeError)


if __name__ == '__main__':
    unittest.main()
