#!/usr/bin/env python3
"""This module define a function of int or float parameter"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """function to_kv that takes a string k and an
    int OR float v as arguments"""
    return (k, v ** 2)
