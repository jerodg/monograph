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


# todo: need tests
# todo: graph this
class Circle(object):
    def __init__(self, x: Union[int, float], y: Union[int, float], r: Union[int, float]):
        if r < 0:
            raise ValueError("Invalid input: radius must be positive")
        self.x = x
        self.y = y
        self.r = r

    def check_relation(self, other_circle) -> str:
        d = math.sqrt((self.x - other_circle.x) ** 2 + (self.y - other_circle.y) ** 2)

        if d <= self.r - other_circle.r:
            return "other_circle is in this circle"
        elif d <= other_circle.r - self.r:
            return "this circle is in other_circle"
        elif d < self.r + other_circle.r:
            return "this circle and other_circle intersect"
        elif d == self.r + other_circle.r:
            return "this circle and other_circle will touch"
        else:
            return "this circle and other_circle do not overlap, intersect, or touch"


def check_circles(
    x0: Union[int, float],
    y0: Union[int, float],
    r0: Union[int, float],
    x1: Union[int, float],
    y1: Union[int, float],
    r1: Union[int, float],
) -> str:
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
