#!/usr/bin/env python3
"""
This module contains an asynchronous generator function.
"""

import asyncio  # Import asyncio for asynchronous operations
import random  # Import random to generate random numbers
from typing import AsyncGenerator  # Import AsyncGenerator for type hinting


async def async_generator() -> AsyncGenerator[float, None]:
    """
    An asynchronous generator that yields a random float between 0 and 10.

    Yields:
        float: A random float between 0 and 10.
    """
    for _ in range(10):  # Loop 10 times
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.uniform(0, 10)  # Yield a random float between 0 and 10
