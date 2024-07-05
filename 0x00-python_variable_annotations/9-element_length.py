#!/usr/bin/env python3
"""This module define anootated function"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return appropiate value type"""
    return [(i, len(i)) for i in lst]
