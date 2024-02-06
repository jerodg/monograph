#!/usr/bin/env python3
"""Python Monograph: Two Sum Solution

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


def method_0(nums: list[int], target: int) -> list[int]:
    """Method 0: Brute Force (iteration)

    Args:
        nums (list[int]):
        target (int):

    Returns:
        list[int]:
    """
    for i, n in enumerate(nums):
        for j, m in enumerate(nums[i + 1:]):
            if n + m == target:
                return [i, j + i + 1]


def method_1(nums: list[int], target: int) -> list[int]:
    """Method 1: Two-pass Hash Table

    Args:
        nums (list[int]):
        target (int):

    Returns:
        list[int]

    """
    d = {}
    for i, n in enumerate(nums):
        d[n] = i

    for i, n in enumerate(nums):
        if target - n in d and i != d[target - n]:
            return [i, d[target - n]]


def method_2(nums: list[int], target: int) -> list[int]:
    """

    Args:
        nums (list[int]):
        target (int):

    Returns:
        list[int]
    """
    d = {}
    for i, n in enumerate(nums):
        if target - n in d:
            return [d[target - n], i]
        d[n] = i


if __name__ == "__main__":
    print(__doc__)
