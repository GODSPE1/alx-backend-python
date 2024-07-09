#!/usr/bin/env python3
"""This module defines an asynchronous function
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that waits for a random
    delay between min_delay and max_delay.

    Args:
        max_delay (int): Maximum delay value (default: 10)

    Returns:
        float: The actual delay value
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
