#!/usr/bin/env python3
"""This module defines an anotated multiplier function"""
from typing import Callable


def make_multiplier(multipier: float) -> Callable[[float], float]:
    """returns the multiplier by a float"""

    def multiplier_function(val: float) -> float:
        return val * multipier
    return multiplier_function