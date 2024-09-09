#!/usr/bin/env python3
"""Test Cases for utils.py. utils.py provides functionality across different,
modules or parts of the application"""
import unittest
from parameterized import parameterized
from utils import memoize, access_nested_map, get_json
from unittest.mock import patch, Mock


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

    @parameterized.expand([
        ({}, ["a"]),
        ({"a": 1}, ["a", "b"]),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """This version of the test still ensures that a KeyError is raised
        and the message includes the correct key"""
        with self.assertRaises(KeyError) as nest:
            access_nested_map(nested_map, path)
        self.assertTrue("'{}'".format(path[-1]) in str(nest.exception))


class TestGetJson(unittest.TestCase):
    """ The @parameterized.expand is used to provide multiple sets of
    arguments to a test method
    The @patch replaces the requests.get with a mock objectinside the
    test method """
    @parameterized.expand([
                ("http://example.com", {"payload": True}),
                ("http://holberton.io", {"payload": False}),
                ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Each test case, a Mock object is created, the requests.get
        return value. The json of the mock object is set to return
        the corresponding test_payload"""
        a = Mock()
        load = test_payload
        url = test_url
        a.json.return_value = load
        mock_get.return_value = a
        result = get_json(url)
        mock_get.assert_called_once_with(url)
        self.assertEqual(result, load)


class TestClass:
    """TestClass has two methods"""

    def a_method(self):
        """a_method simply returns 42"""
        return 42

    @memoize
    def a_property(self):
        """a_property a method with @memoize means its result will be
        cached after the first call"""
        return self.a_method()


class TestMemoize(unittest.TestCase):

    @patch.object(TestClass, 'a_method', return_value=42)
    def test_memoize(self, mock_a_method):
        """obj = TestClass() create an instance of TestClass, data1 or data2
        access a_property for the first time and this will invoke a_method
        and cache the result."""
        obj = TestClass()

        data1 = obj.a_property
        self.assertEqual(data1, 42)
        mock_a_method.assert_called_once()

        data2 = obj.a_property
        self.assertEqual(data2, 42)
        mock_a_method.assert_called_once()
