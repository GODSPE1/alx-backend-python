#!/usr/bin/env python3
"""Unit tests for access_nested_map function"""
import unittest
from parameterized import parameterized

def access_nested_map(nested_map: dict, path: tuple) -> object:
    """Access nested value in a map using the specified path."""
    current = nested_map
    for key in path:
        current = current[key]
    return current

# Define the test class
@parameterized.expand([
    {"nested_map": {"a": 1}, "path": ("a",)},
    {"nested_map": {"a": {"b": 2}}, "path": ("a",)},
    {"nested_map": {"a": {"b": 2}}, "path": ("a", "b")}
])
class TestAccessNestedMap(unittest.TestCase):
    def test_access_existing_path(self, nested_map: dict, path: tuple) -> None:
        """Test access_nested_map function with existing path."""
        expected_result = path[-1]
        actual_result = access_nested_map(nested_map, path)
        self.assertEqual(actual_result, expected_result)

if __name__ == "__main__":
    unittest.main()
