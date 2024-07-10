#!/usr/bin/env python3
"""Import async_comprehension from the previous file and write
a measure_runtime coroutine that will execute async_comprehension four
times in parallel using asyncio.gather. measure_runtime should
measure the total runtime and return it.
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the run time"""
    start_time = time.time()
    awaitables = [async_comprehension() for i in range(4)]
    results = await asyncio.gather(*awaitables)
    end_time = time.time()

    return end_time - start_time
