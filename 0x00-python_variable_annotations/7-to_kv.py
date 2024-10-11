#!/usr/bin/env python3
"""
this module returns float
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function to return a tuple with a string and the square of an int/float.

    Args:
        k (str): The string.
        v (Union[int, float]): The int or float number.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string k,
        and the second element is the square of v as a float.
    """
    return (k, float(v ** 2))
