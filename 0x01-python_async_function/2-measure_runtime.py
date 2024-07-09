#!/usr/bin/env python3
"""This module defines an asynchronous function
"""

import random
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n

async def measure_time(n: int, max_delay: int) -> float:
    start_time = time.time()

    await wait_n(n, max_delay)

    end_time = time.time()
    total_execution_time = end_time - start_time
    
    average_time_per_task = total_execution_time / n 
    return average_time_per_task