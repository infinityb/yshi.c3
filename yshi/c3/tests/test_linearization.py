# The MIT License (MIT)
#
# Copyright (c) 2013 Yasashii Syndicate
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import unittest
from yshi.c3 import InconsistentHierarchy, linearize


class_parent_func = lambda x: x.__bases__
dict_parent_func = lambda p: (lambda x: p[x])


class C3LinearizationTest(unittest.TestCase):
    maxDiff = None

    def test_inconsistent_hierarchy(self):
        """Serious order disagreement"""  # From Guido
        parent_dict = {
            'O': [],
            'X': ['O'],
            'Y': ['O'],
            'A': ['X', 'Y'],
            'B': ['Y', 'X'],
            'Z': ['A', 'B']
        }
        with self.assertRaises(InconsistentHierarchy):
            linearize(dict_parent_func(parent_dict), 'Z')

    def test_example_one(self):
        """My first example"""
        parent_dict = {
            'O': [],
            'F': ['O'],
            'E': ['O'],
            'D': ['O'],
            'C': ['D', 'F'],
            'B': ['D', 'E'],
            'A': ['B', 'C']
        }
        self.assertEqual(
            linearize(dict_parent_func(parent_dict), 'A'),
            ['A', 'B', 'C', 'D', 'E', 'F', 'O']
        )
        self.assertEqual(
            linearize(dict_parent_func(parent_dict), 'B'),
            ['B', 'D', 'E', 'O']
        )

    def test_example_two(self):
        """My second example"""
        parent_dict = {
            'O': [],
            'F': ['O'],
            'E': ['O'],
            'D': ['O'],
            'C': ['D', 'F'],
            'B': ['E', 'D'],
            'A': ['B', 'C']
        }
        self.assertEqual(
            linearize(dict_parent_func(parent_dict), 'C'),
            ['C', 'D', 'F', 'O']
        )
        self.assertEqual(
            linearize(dict_parent_func(parent_dict), 'B'),
            ['B', 'E', 'D', 'O']
        )
        self.assertEqual(
            linearize(dict_parent_func(parent_dict), 'A'),
            ['A', 'B', 'E', 'C', 'D', 'F', 'O']
        )

    def test_example_three(self):
        parent_dict = {
            'O': [],
            'A': ['O'],
            'B': ['O'],
            'C': ['O'],
            'D': ['O'],
            'E': ['O'],
            'K1': ['A', 'B', 'C'],
            'K2': ['D', 'B', 'E'],
            'K3': ['D', 'A'],
            'Z': ['K1', 'K2', 'K3']
        }
        self.assertEqual(
            linearize(dict_parent_func(parent_dict), 'K1'),
            ['K1', 'A', 'B', 'C', 'O']
        )
        self.assertEqual(
            linearize(dict_parent_func(parent_dict), 'K2'),
            ['K2', 'D', 'B', 'E', 'O']
        )
        self.assertEqual(
            linearize(dict_parent_func(parent_dict), 'K3'),
            ['K3', 'D', 'A', 'O']
        )
        self.assertEqual(
            linearize(dict_parent_func(parent_dict), 'Z'),
            ['Z', 'K1', 'K2', 'K3', 'D', 'A', 'B', 'C', 'E', 'O']
        )

