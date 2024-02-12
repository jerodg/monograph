#!/usr/bin/env python3
"""Python Monograph:

Copyright ©2024 Jerod Gawne <https://github.com/jerodg/>

This program is free software: you can redistribute it and/or modify
it under the terms of the Server Side Public License (SSPL) as
published by MongoDB, Inc., either version 1 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
SSPL for more details.

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
You should have received a copy of the SSPL along with this program.
If not, see <https://www.mongodb.com/licensing/server-side-public-license>."""
from collections import ChainMap
from itertools import chain
from collections import defaultdict


def method_0(x: dict, y: dict) -> dict:
    """Copy->Update

    Args:
        x: dict
        y: dict

    Returns:
        dict
    """
    temp = x.copy()
    temp.update(y)
    return temp


def method_1(x: dict, y: dict) -> dict:
    """Add Items

    Args:
        x: dict
        y: dict

    Returns:
        dict
    """
    return dict(list(x.items()) + list(y.items()))


def method_2(x: dict, y: dict) -> dict:
    """Curly Star
        - Requires Python 3.5+

    Args:
        x: dict
        y: dict

    Returns:
        dict
    """
    return {**x, **y}


def method_3(x: dict, y: dict) -> dict:
    """Chain Map

    Args:
        x: dict
        y: dict

    Returns:
        dict
    """
    return dict(ChainMap({}, y, x))


def method_4(x: dict, y: dict) -> dict:
    """Itertools Chain

    Args:
        x: dict
        y: dict

    Returns:
        dict
    """
    return dict(chain(x.items(), y.items()))


def method_5(x: dict, y: dict) -> dict:
    """Python3.9+ Concat
       - Requires Python 3.9+

    Args:
        x: dict
        y: dict

    Returns:
        dict
    """
    return x | y


def method_6(x: dict, y: dict) -> dict:
    """

    Args:
        x: dict
        y: dict

    Returns:
        dict
    """
    return next(z.update(y) or z for z in [x.copy()])


def method_7(x: dict, y: dict) -> dict:
    """

    Args:
        x: dict
        y: dict

    Returns:
        dict
    """
    return (lambda z: z.update(y) or z)(x.copy())


def method_8(x: dict, y: dict) -> dict:
    """Dictionary Comprehension

    Args:
        x: dict
        y: dict

    Returns:
        dict
    """
    return {k: v for d in [x, y] for k, v in d.items()}


def method_9(x: dict, y: dict) -> dict:
    """Update Method

    Args:
        x: dict
        y: dict

    Returns:
        dict
    """
    x.update(y)
    return x


def method_10(x: dict, y: dict) -> dict:
    """DefaultDict Method

    Args:
        x: dict
        y: dict

    Returns:
        dict
    """
    merged = defaultdict(list)
    for d in (x, y):
        for key, value in d.items():
            merged[key].append(value)
    return merged


if __name__ == "__main__":
    print(__doc__)
