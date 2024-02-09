#!/usr/bin/env python3
"""Python Monograph: Find Unique Keys from a List of Dicts

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
from functools import reduce
from itertools import chain
from typing import List


def method_0(arr: List[dict]) -> list:
    """Method 0: Using Chain itertools

    Args:
            arr (List[dict]):

    Returns:
            (list)"""
    return list(set(chain.from_iterable(sub.keys() for sub in arr)))


def method_1(arr: List[dict]) -> list:
    """Method 1: Using list/dict Comprehension

    Args:
            arr (List[dict]):

    Returns:
            (list)"""
    return list(set(val for dic in arr for val in dic.keys()))


def method_2(arr: List[dict]) -> list:
    """Method 2: Using keys(),extend(),list() and set() methods

    Args:
            arr (List[dict]):

    Returns:
            (list)"""
    new_list = []

    for i in arr:
        new_list.extend(list(i.keys()))

    return list(set(new_list))


def method_3(arr: List[dict]) -> list:
    """Method 3: Using functools.reduce()

    Args:
            arr (List[dict]):

    Returns:
            (list)"""
    return list(reduce(lambda a, b: {**a, **b}, arr).keys())


if __name__ == "__main__":
    print(__doc__)
