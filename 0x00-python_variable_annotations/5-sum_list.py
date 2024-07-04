#!/usr/bin/env python3
"""This module defines typed-annotated sum function
"""
from typing import List


def sum_list(n: List[float]) -> float:
    """function returns the string of value passed"""
    total = sum(n)
    return float(total)
