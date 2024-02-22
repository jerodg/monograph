#!/usr/bin/env python3
"""Python Monograph: Test Array Shuffling

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
from python_monograph.array_shuffling.solution import method_0, method_1


def test_method_0_happy_path():
    assert method_0([-1, 0, 1, -1, 5, 10, -5]) == [-1, 5, -1, 10, 0, 1, -5]
    assert method_0([2, 5, 1, 3, 4]) == [1, 5, 2, 4, 3]


def test_method_0_edge_cases():
    assert method_0([]) == []
    assert method_0([1]) == [1]
    assert method_0([1, 2]) == [1, 2]
    assert method_0([2, 1]) == [1, 2]


def test_method_1_happy_path():
    assert method_1([-1, 0, 1, -1, 5, 10, -5]) == [-1, 5, -1, 10, 0, 1, -5]
    assert method_1([2, 5, 1, 3, 4]) == [1, 5, 2, 4, 3]


def test_method_1_edge_cases():
    assert method_1([]) == []
    assert method_1([1]) == [1]
    assert method_1([1, 2]) == [1, 2]
    assert method_1([2, 1]) == [1, 2]


def test_method_2_happy_path():
    assert method_0([-1, 0, 1, -1, 5, 10, -5]) == [-1, 5, -1, 10, 0, 1, -5]
    assert method_0([2, 5, 1, 3, 4]) == [1, 5, 2, 4, 3]


def test_method_2_edge_cases():
    assert method_1([]) == []
    assert method_1([1]) == [1]
    assert method_1([1, 2]) == [1, 2]
    assert method_1([2, 1]) == [1, 2]


if __name__ == "__main__":
    print(__doc__)
