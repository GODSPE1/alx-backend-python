#!/usr/bin/env python3
"""This module defines an asynchronous function
"""

import random
import asyncio
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    """returns sorted list."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """returs sorted list"""

    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
