#!/usr/bin/env python3
"""Module that defines an async generator yielding random numbers."""


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Yieldrandom number between 0, 10, ten times with 1s delay."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
