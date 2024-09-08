#!/usr/bin/env python3
"""Test Cases for utils.py. utils.py provides functionality across different,
modules or parts of the application"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """The @parameterized.expand decorator allows test for multiple sets
    inputs"""
    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2),
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ nested_map is a dictionary,that can contain other dictionaries,
        path is a sequence of key that of keys that represent the path"""
        test = access_nested_map(nested_map, path)
        self.assertEqual(test, expected)
