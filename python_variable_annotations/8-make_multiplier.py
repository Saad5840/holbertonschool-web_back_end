#!/usr/bin/env python3
"""Module that provides a function returning a multiplier function."""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by the given multiplier."""
    def multiplier_func(x: float) -> float:
        return x * multiplier

    return multiplier_func
