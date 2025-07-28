#!/usr/bin/env python3
"""Module that defines a coroutine to collect random numbers asynchronously."""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers from async_generator using comprehension."""
    return [num async for num in async_generator()]
