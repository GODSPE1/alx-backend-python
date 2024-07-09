#!/usr/bin/env python3
"""This module defines an Async Generator"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """This is a coroutine called async_generator that takes no arguments."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
