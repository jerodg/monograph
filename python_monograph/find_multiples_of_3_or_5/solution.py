#!/usr/bin/env python3
"""Python Monograph: Find Multiples of 3 and 5 Solutions

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


def method_0() -> int:
    """This function calculates and prints the sum of all multiples of 3 or 5 below 1000 using a for loop.

    Returns:
        int
    """
    sum = 0
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    return sum


def method_1() -> int:
    """This function calculates and prints the sum of all multiples of 3 or 5 below 1000 using list comprehension.

    Returns:
        int
    """
    return sum(i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0)


def method_2() -> int:
    """This function calculates and prints the sum of all multiples of 3 or 5 below 1000 using a mathematical approach.

    Returns:
        None
    """

    def sum_divisible_by(n: int) -> int:
        p = 999 // n
        return n * (p * (p + 1)) // 2

    return sum_divisible_by(3) + sum_divisible_by(5) - sum_divisible_by(15)


if __name__ == "__main__":
    print(__doc__)
