#!/usr/bin/env python3
"""Python Monograph: Flatten a List of Lists or Tuples

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
from functools import reduce
from typing import Generator

import numpy as np


def method_0(itr: (tuple, list)) -> Generator:
    """Method 0: Using a generator w/ recursion

    Notes:
            Does not provide the location of the substr.

    Args:
            itr (tuple|list):

    Returns:
            object (generator):

    References:
            https://docs.python.org/3/reference/expressions.html#yieldexpr"""
    for item in itr:
        if isinstance(item, (tuple, list)):
            yield from method_0(item)
        else:
            yield item


def method_1(itr: (tuple, list)) -> list:
    """Method 1: Using itertools.chain

    :param itr:
    :return:
    """
    return list(itertools.chain(*itr))


def method_2(itr: (tuple, list)) -> list:
    """Method 2: Using list comprehension

    :param itr:
    :return:
    """
    return [item for sublist in itr for item in sublist]


def method_3(itr: (tuple, list)) -> list:
    """Method 3: Using numpy

    :param itr:
    :return:
    """
    return np.array(itr).flatten().tolist()


def method_4(itr: (tuple, list)) -> list:
    """Method 4: Using reduce

    :param itr:
    :return:
    """
    return reduce(lambda x, y: x + y, itr)


if __name__ == "__main__":
    print(__doc__)
