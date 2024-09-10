#!/usr/bin/env python3
"""Testing Client.py"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """The TestGithubOrgClient class and test_org method,
    @parameterized.expand decorator test the names "google" and "adc" """
    @parameterized.expand([
        ("google",),
        ("abc",),
        ])
    @patch('client.get_json')
    def test_org(self, org_name, get_json):
        """The test_org method run twice once for "google" and once for "abc"
        Each time the get_json method is mocked to return a response"""
        result = GithubOrgClient(org_name)
        mock_value = {"login": org_name, "id": 12345}
        get_json.return_value = mock_value
        a = result.org
        Url = "https://api.github.com/orgs/{}".format(org_name)
        get_json.assert_called_once_with(Url)
        self.assertEqual(a, mock_value)
