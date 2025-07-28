#!/usr/bin/env python3
"""Module that provides function returning tuple with key and squared value."""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return tuple, the first element is k, the second is v squared as float."""
    return (k, float(v ** 2))
