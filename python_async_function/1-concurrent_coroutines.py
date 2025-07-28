#!/usr/bin/env python3
"""Module to concurrently spawn wait_random n times and return sorted delays."""

import asyncio
from typing import List
from 0_basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with max_delay and return sorted list of delays."""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
