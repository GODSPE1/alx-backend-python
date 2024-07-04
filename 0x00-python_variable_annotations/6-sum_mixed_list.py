#!/usr/bin/env python3
"""This module defines typed-annotated sum function
"""
from typing import List, Union


def sum_mixed_list(n: List[Union[int, float]]) -> float:
    """function returns the sum of varied int numbers"""
    total = sum(n)
    return float(total)
