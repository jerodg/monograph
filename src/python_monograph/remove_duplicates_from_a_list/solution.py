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
import itertools
import operator
from collections import OrderedDict

import numpy as np
import pandas as pd


def method_0(ls: list) -> list:
    """Remove duplicates from a list using a set.

    This function takes a list as input and returns a new list that contains the unique elements from the input list.
    The function uses a set to remove duplicates, which does not preserve the order of elements.
    The original list is not modified.

    Args:
        ls: The list from which duplicates should be removed.

    Returns:
        A new list that contains the unique elements from the input list.
    """
    return list(set(ls))


def method_1(ls: list) -> list:
    """Remove duplicates from a list using set and *arg expansion.

    This function takes a list as input and returns a new list that contains the unique elements from the input list.
    The function uses set and *arg expansion to remove duplicates, which does not preserve the order of elements.
    The original list is not modified.

    Args:
        ls: The list from which duplicates should be removed.

    Returns:
        A new list that contains the unique elements from the input list.
    """
    return [*{*ls}]


def method_2(ls: list) -> list:
    """Remove duplicates from a list using set and list comprehension.

    This function takes a list as input and returns a new list that contains the unique elements from the input list.
    The function uses set and list comprehension to remove duplicates, which does not preserve the order of elements.
    The original list is not modified.

    Args:
        ls: The list from which duplicates should be removed.

    Returns:
        A new list that contains the unique elements from the input list.
    """
    unique = set()
    return list([unique.add(n) or n for n in ls if n not in unique])


def method_3(ls: list) -> list:
    """Remove duplicates from a list using list comprehension.

    This function takes a list as input and returns a new list that contains the unique elements from the input list.
    The function uses list comprehension to remove duplicates, which preserves the order of elements and keeps the first
    occurrence of each element.
    The original list is not modified.

    Args:
        ls: The list from which duplicates should be removed.

    Returns:
        A new list that contains the unique elements from the input list.
    """
    return [ii for n, ii in enumerate(ls) if ii not in ls[:n]]


def method_4(ls: list) -> list:
    """Remove duplicates from a list using a for-loop.

    This function takes a list as input and returns a new list that contains the unique elements from the input list.
    The function uses a for-loop to remove duplicates, which preserves the order of elements and keeps the first occurrence of
    each element.
    The original list is not modified.

    Args:
        ls: The list from which duplicates should be removed.

    Returns:
        A new list that contains the unique elements from the input list.
    """
    unique = []
    for item in ls:
        if item not in unique:
            unique.append(item)

    return unique


def method_5(ls: list) -> list:
    """Remove duplicates from a list using list comprehension, preserving order and keeping the last occurrence.

    This function takes a list as input and returns a new list that contains the unique elements from the input list.
    The function uses list comprehension to remove duplicates, which preserves the order of elements and keeps the last
    occurrence of each element.
    The original list is not modified.

    Args:
        ls: The list from which duplicates should be removed.

    Returns:
        A new list that contains the unique elements from the input list.
    """
    return [a for i, a in enumerate(ls) if a not in ls[i + 1 :]]


def method_6(ls: list) -> list:
    """Remove duplicates from a list using dict.

    This function takes a list as input and returns a new list that contains the unique elements from the input list.
    The function uses dict to remove duplicates, which preserves the order of elements and keeps the first occurrence of each
    element.
    The original list is not modified.

    Args:
        ls: The list from which duplicates should be removed.

    Returns:
        A new list that contains the unique elements from the input list.
    """
    return list(dict.fromkeys(ls))


def method_7(ls: list) -> list:
    """Remove duplicates from a list using pandas.

    This function takes a list as input and returns a new list that contains the unique elements from the input list.
    The function uses pandas Series and the drop_duplicates method to remove duplicates, which preserves the order of elements
    and keeps the first occurrence of each element.
    The original list is not modified.

    Args:
        ls: The list from which duplicates should be removed.

    Returns:
        A new list that contains the unique elements from the input list.
    """
    return pd.Series(ls).drop_duplicates().tolist()


def method_8(ls: list) -> list:
    """Remove duplicates from a list using numpy.

    This function takes a list as input and returns a new list that contains the unique elements from the input list.
    The function uses numpy's unique function to remove duplicates, which does not preserve the order of elements.
    The original list is not modified.

    Args:
        ls: The list from which duplicates should be removed.

    Returns:
        A new list that contains the unique elements from the input list.
    """
    return np.unique(ls).tolist()


# fixme: this is broken
def method_9(ls: list) -> list:
    """Remove duplicates from a list using itertools.groupby.

    This function takes a list as input and returns a new list that contains the unique elements from the input list.
    The function uses itertools.groupby to remove duplicates, which does not preserve the order of elements.
    The original list is not modified.

    Args:
        ls: The list from which duplicates should be removed.

    Returns:
        A new list that contains the unique elements from the input list.
    """
    return [next(g) for _, g in itertools.groupby(sorted(ls, key=operator.itemgetter(0))) if g]


def method_10(ls: list) -> list:
    """Remove duplicates from a list using OrderedDict.

    This function takes a list as input and returns a new list that contains the unique elements from the input list.
    The function uses OrderedDict to remove duplicates, which preserves the order of elements and keeps the first occurrence of
    each element.
    The original list is not modified.

    Args:
        ls: The list from which duplicates should be removed.

    Returns:
        A new list that contains the unique elements from the input list.
    """
    return list(OrderedDict.fromkeys(ls))


if __name__ == '__main__':
    print(__doc__)
