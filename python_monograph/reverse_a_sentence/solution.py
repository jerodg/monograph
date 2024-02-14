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
import re
from functools import reduce

def method_0(sentence: str) -> str:
    """Method 0: Reversed
        - Reverses the entire sentence

    Args:
        sentence: (str)

    Returns:
        result: (str)"""
    return "".join(reversed(sentence))


def method_1(sentence: str) -> str:
    """Method 1: Regex
        - Reverse the letters of each word, preserving word-order.

    Args:
        sentence: (str)

    Returns:
        result: (str)"""
    return re.sub(r"(\w+)", lambda x: x.group()[::-1], sentence)


def method_2(sentence: str) -> str:
    """Method 2: Slice

    Args:
        sentence: (str)

    Returns:
        result: (str)"""
    return sentence[slice(None, None, -1)]


def method_3(sentence: str) -> str:
    """Method 3: Shorthand slice

    Args:
        sentence: (str)

    Returns:
        result: (str)"""
    return sentence[::-1]


def method_4(sentence: str) -> str:
    """Method 4: List comprehension
        - Changes word order only
    Args:
        sentence: (str)

    Returns:
        result: (str)"""
    s = sentence.split()
    l = []
    for i in s:
        l.append(i)

    res = [ii for n, ii in enumerate(l) if ii not in l[:n]]
    return " ".join(res[::-1])

def method_5(sentence: str) -> str:
    """Method 5 - Using split and join

    :param sentence:
    :type sentence:
    :return:
    :rtype:
    """
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

def method_6(sentence: str) -> str:
    """Method 6 - Using list comprehension alternate

    :param sentence:
    :type sentence:
    :return:
    :rtype:
    """
    return ' '.join(word for word in sentence.split()[::-1])


def method_7(sentence: str) -> str:
    """Method 7 - Using reduce

    :param sentence:
    :type sentence:
    :return:
    :rtype:
    """
    return reduce(lambda x, y: y + ' ' + x, sentence.split())


if __name__ == "__main__":
    print(__doc__)
