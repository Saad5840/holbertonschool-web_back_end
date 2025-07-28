#!/usr/bin/env python3
"""Module that provides a function returning a tuple with a key and squared value."""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple where the first element is k and the second is v squared as a float."""
    return (k, float(v ** 2))
