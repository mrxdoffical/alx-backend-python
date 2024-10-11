#!/usr/bin/env python3
"""
This module provides a function to safely get values from a dictionary.
"""


from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, Any],
                     key: Any, default: Union[T, None]
                     = None) -> Union[Any, T]:
    """
    Function to safely get a value from a dictionary.

    Args:
        dct (Mapping[Any, Any]): The dictionary to get the value from.
        key (Any): The key to search for in the dictionary.
        default (Union[T, None]):
        The default value to return if the key is not found.

    Returns:
        Union[Any, T]: The value from the dictionary if the key is found,
        otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
