#!/usr/bin/env python3
"""Unit and Integration Tests for Utility Functions"""
from parameterized import parameterized
from typing import Any, Mapping, Sequence
from unittest import TestCase


def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    current = nested_map
    for key in path:
        if key in current:
            current = current[key]
        else:
            raise KeyError(f"Key {key} not found in map")
        if not isinstance(current, dict) and key != path[-1]:
            raise TypeError(f"Expected a dict at key {key},\
                            got {type(current).__name__}")
    return current


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
        """Test that access_nested_map returns the correct value"""
        self.assertEqual(access_nested_map(nested_dict, path), expected_value)

    @parameterized.expand([
        ({"a": 1}, ("a", "b")),
        ({}, ("a",)),
    ])
    def test_access_nested_map_exception(
            self, nested_dict: Mapping, path: Sequence):
        """Test that access_nested_map raises KeyError for invalid paths"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_dict, path)


if __name__ == '__main__':
    unittest.main()
