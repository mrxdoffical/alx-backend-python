#!/usr/bin/env python3
"""
this module is safe for fitst element
"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Function to safely return the first element of a sequence, if it exists.

    Args:
        lst (Sequence[Any]): A sequence of any type.

    Returns:
        Union[Any, None]:
        The first element of the sequence if it exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
