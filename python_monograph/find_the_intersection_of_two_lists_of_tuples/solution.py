#!/usr/bin/env python3
"""Python Monograph: Find the Intersection of Two Lists of Tuples Solution

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

def method_0(ls0: list, ls1: list) -> set:
    """Using sorted(), set(), and list comprehension

    :param ls0: (list)
    :param ls1: (list)
    :return: (set)"""
    return set([tuple(sorted(x)) for x in ls0]) & set([tuple(sorted(y)) for y in ls1])


def method_1(ls0: list, ls1: list) -> set:
    """Using list comprehension, map(), frozenset(), and &

    :param ls0: (list)
    :param ls1: (list)
    :return: (set)"""
    return set(map(frozenset, ls0)) & set(map(frozenset, ls1))


def method_2(ls0: list, ls1: list) -> list:
    """Using list comprehension

    :param ls0: (list)
    :param ls1: (list)
    :return: (list)"""
    return [x for x in ls0 for y in ls1 if x == y]


def method_3(ls0: list, ls1: list) -> list:
    """Using set.intersection()

    :param ls0: (list)
    :param ls1: (list)
    :return: (list)"""
    return list(set(ls0).intersection(set(ls1)))

def method_4(ls0: list, ls1: list) -> list:
    """Using a List Comprehension with in Operator

    :param ls0: (list)
    :param ls1: (list)
    :return: (list)"""
    return [x for x in ls0 if x in ls1]

def method_5(ls0: list, ls1: list) -> list:
    """Using the filter() Function

    :param ls0:
    :param ls1:
    :return: """
    return list(filter(lambda x: x in ls1, ls0))

def method_6(ls0: list, ls1: list) -> list:
    """Using a Set Comprehension

    :param ls0: (list)
    :param ls1: (list)
    :return: (list)"""
    return list({x for x in ls0}.intersection(ls1))

if __name__ == "__main__":
    print(__doc__)
