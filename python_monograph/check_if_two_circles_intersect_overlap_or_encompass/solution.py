#!/usr/bin/env python3
"""Python Monograph: Check if Two Circles Intersect, Overlap, or Encompass

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
import math
from typing import Union


def check_circles(
    x0: Union[int, float],
    y0: Union[int, float],
    r0: Union[int, float],
    x1: Union[int, float],
    y1: Union[int, float],
    r1: Union[int, float],
) -> str:
    """Method 0: If Conditional

    :param x0: Union[int, float]
    :param y0: Union[int, float]
    :param r0: Union[int, float]
    :param x1: Union[int, float]
    :param y1: Union[int, float]
    :param r1: Union[int, float]
    :return: str"""
    if r0 < 0 or r1 < 0:
        return "Invalid input: radius must be positive"

    d = math.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)

    if d <= r0 - r1:
        return "c1 is in c0"
    elif d <= r1 - r0:
        return "c0 is in c1"
    elif d < r0 + r1:
        return "c0 and c1 intersect"
    elif d == r0 + r1:
        return "c0 and c1 will touch"
    else:
        return "c0 and c1 do not overlap, intersect, or touch"


if __name__ == "__main__":
    print(__doc__)
