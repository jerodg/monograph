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
from collections import OrderedDict

import numpy as np
import pandas as pd


def method_0(ls: list) -> list:
    """Method 0: Set
        Doesn't preserve order

    Args:
        ls: (list)

    Returns:
        result: (list)"""
    return list(set(ls))


def method_1(ls: list) -> list:
    """Method 1: *arg expansion
        Doesn't preserve order

    Args:
        ls: (list)

    Returns:
        result: (list)"""
    return [*{*ls}]


def method_2(ls: list) -> list:
    """Method 2: Set/List comprehension
        Doesn't preserve order

    Args:
        ls: (list)

    Returns:
        result: (list)"""
    unique = set()
    return list([unique.add(n) or n for n in ls if n not in unique])


def method_3(ls: list) -> list:
    """Using list comprehension
    Method 3:
        Preserves order; keeps first occurance

    Args:
        ls: (list)

    Returns:
        result: (list)"""
    return [ii for n, ii in enumerate(ls) if ii not in ls[:n]]


def method_4(ls: list) -> list:
    """Method 4: for-loop
        Preserves order; keeps first occurance

    Args:
        ls: (list)

    Returns:
        result: (list)"""
    unique = []
    for item in ls:
        if item not in unique:
            unique.append(item)

    return unique


def method_5(ls: list) -> list:
    """Method 5: list comprehension alternate
        Preserves order; keeps last occurance

    Args:
        ls: (list)

    Returns:
        result: (list)"""
    return [a for i, a in enumerate(ls) if a not in ls[i + 1 :]]


def method_6(ls: list) -> list:
    """Method 6: dict
        Preserves order; keeps first occurance

    Args:
        ls: (list)

    Returns:
        result: (list)"""
    return list(dict.fromkeys(ls))


def method_7(ls: list) -> list:
    """Using pandas

    :param ls:
    :type ls:
    :return:
    :rtype:
    """
    return pd.Series(ls).drop_duplicates().tolist()


def method_8(ls: list) -> list:
    """Using numpy

    :param ls:
    :type ls:
    :return:
    :rtype:
    """
    return np.unique(ls).tolist()


# fixme: this is broken
# def method_9(ls: list) -> list:
#     """Using itertools.groupby
#
#     :param ls:
#     :type ls:
#     :return:
#     :rtype:
#     """
#     return [next(g) for _, g in itertools.groupby(sorted(ls, key=operator.itemgetter(0))) if g]


def method_10(ls: list) -> list:
    """Using OrderedDict

    :param ls:
    :type ls:
    :return:
    :rtype:
    """
    return list(OrderedDict.fromkeys(ls))


if __name__ == "__main__":
    print(__doc__)
