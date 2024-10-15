#!/usr/bin/env python3
"""
this module do something with tasks
"""


import asyncio
from typing import Any, Union
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task for the wait_random coroutine.

    Args:
        max_delay (int): Maximum delay value.

    Returns:
        asyncio.Task: A task object for the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
