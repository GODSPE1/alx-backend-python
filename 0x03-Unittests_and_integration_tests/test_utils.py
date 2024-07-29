#!/usr/bin/env python3
"""Unit and Integration Tests for Utility Functions"""

from parameterized import parameterized
from typing import Mapping, Sequence
from unittest import TestCase


class TestAccessNestedMap(TestCase):
    """Unit tests for access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self, nested_dict: Mapping, path: Sequence, expected_value: Any
            ):
        "Test that access_nested_map returns the correct value"""
        self.assertEqual(access_nested_map(nested_dict, path), expected_value)

