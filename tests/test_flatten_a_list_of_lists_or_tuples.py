#!/usr/bin/env python3
"""Python Monograph: Test Flatten a List of Lists or Tuples

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
from python_monograph.flatten_a_list_of_lists_or_tuples.solution import method_0, method_1, method_2, method_3, method_4


def test_method_0_flattens_nested_lists():
    assert list(method_0([1, [2, 3], [4, [5, 6]]])) == [1, 2, 3, 4, 5, 6]


def test_method_0_handles_empty_lists():
    assert list(method_0([])) == []


def test_method_1_flattens_lists():
    assert method_1([[1, 2], [3, 4]]) == [1, 2, 3, 4]


def test_method_1_handles_empty_lists():
    assert method_1([]) == []


def test_method_2_flattens_lists():
    assert method_2([[1, 2], [3, 4]]) == [1, 2, 3, 4]


def test_method_2_handles_empty_lists():
    assert method_2([]) == []


def test_method_3_flattens_lists():
    assert method_3([[1, 2], [3, 4]]) == [1, 2, 3, 4]


def test_method_3_handles_empty_lists():
    assert method_3([]) == []


def test_method_4_flattens_lists():
    assert method_4([[1, 2], [3, 4]]) == [1, 2, 3, 4]


# Can't reduce an empty iterable
# def test_method_4_handles_empty_lists():
#     assert method_4([]) == []


if __name__ == "__main__":
    print(__doc__)
