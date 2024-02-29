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

from check_if_two_circles_intersect_overlap_or_encompass import check_circles


def test_circles_intersect():
    assert check_circles(0, 0, 2, 2, 2, 2) == 'c0 and c1 intersect'


def test_one_circle_inside_other():
    assert check_circles(0, 0, 5, 0, 0, 2) == 'c1 is in c0'


def test_circles_touch():
    assert check_circles(0, 0, 2, 0, 4, 2) == 'c0 and c1 will touch'


def test_circles_do_not_overlap():
    assert check_circles(0, 0, 1, 5, 5, 1) == 'c0 and c1 do not overlap, intersect, or touch'


def test_circles_with_same_center():
    assert check_circles(0, 0, 2, 0, 0, 2) == 'c1 is in c0'


def test_circles_with_zero_radius():
    assert check_circles(0, 0, 0, 0, 0, 0) == 'c1 is in c0'


def test_circles_with_negative_radius():
    assert check_circles(0, 0, -2, 2, 2, -2) == 'Invalid input: radius must be positive'


def test_circles_with_same_radius():
    assert check_circles(0, 0, 2, 2, 2, 2) == 'c0 and c1 intersect'


def test_circles_with_large_coordinates():
    assert check_circles(1000000, 1000000, 2, 2000000, 2000000, 2) == 'c0 and c1 do not overlap, intersect, or touch'


def test_circles_with_small_coordinates():
    assert check_circles(0.000001, 0.000001, 0.000002, 0.000002, 0.000002, 0.000002) == 'c0 and c1 intersect'
