#!/usr/bin/env python3
""""""
from typing import Callable


def make_multiplier(multipier: float) -> Callable[[float], float]:
    """"""
    def multiplier_function(val: float) -> float:
        return val * multipier
    return multiplier_function
