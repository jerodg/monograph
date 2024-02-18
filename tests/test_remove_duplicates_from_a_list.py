#!/usr/bin/env python3
"""Python Monograph: Test

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
from python_monograph.remove_duplicates_from_a_list.solution import (
    method_0,
    method_1,
    method_10,
    method_2,
    method_3,
    method_4,
    method_5,
    method_6,
    method_7,
    method_8,
)


def test_method_0_removes_duplicates_without_preserving_order():
    assert method_0([1, 2, 2, 3, 3, 3]) == [1, 2, 3]
    assert method_0([]) == []
    assert method_0([1]) == [1]


def test_method_1_removes_duplicates_without_preserving_order():
    assert method_1([1, 2, 2, 3, 3, 3]) == [1, 2, 3]
    assert method_1([]) == []
    assert method_1([1]) == [1]


def test_method_2_removes_duplicates_without_preserving_order():
    assert method_2([1, 2, 2, 3, 3, 3]) == [1, 2, 3]
    assert method_2([]) == []
    assert method_2([1]) == [1]


def test_method_3_preserves_order_and_keeps_first_occurrence():
    assert method_3([1, 2, 2, 3, 3, 3]) == [1, 2, 3]
    assert method_3([3, 2, 2, 1, 1, 1]) == [3, 2, 1]
    assert method_3([]) == []
    assert method_3([1]) == [1]


def test_method_4_preserves_order_and_keeps_first_occurrence():
    assert method_4([1, 2, 2, 3, 3, 3]) == [1, 2, 3]
    assert method_4([3, 2, 2, 1, 1, 1]) == [3, 2, 1]
    assert method_4([]) == []
    assert method_4([1]) == [1]


def test_method_5_preserves_order_and_keeps_last_occurrence():
    assert method_5([1, 2, 2, 3, 3, 3]) == [1, 2, 3]
    assert method_5([3, 2, 2, 1, 1, 1]) == [3, 2, 1]
    assert method_5([]) == []
    assert method_5([1]) == [1]


def test_method_6_preserves_order_and_keeps_first_occurrence():
    assert method_6([1, 2, 2, 3, 3, 3]) == [1, 2, 3]
    assert method_6([3, 2, 2, 1, 1, 1]) == [3, 2, 1]
    assert method_6([]) == []
    assert method_6([1]) == [1]


def test_method_7_uses_pandas_to_remove_duplicates():
    assert method_7([1, 2, 2, 3, 3, 3]) == [1, 2, 3]
    assert method_7([3, 2, 2, 1, 1, 1]) == [3, 2, 1]
    assert method_7([]) == []
    assert method_7([1]) == [1]


def test_method_8_removes_duplicates_using_numpy():
    assert method_8([1, 2, 2, 3, 3, 3]) == [1, 2, 3]
    assert method_8([3, 2, 2, 1, 1, 1]) == [1, 2, 3]
    assert method_8([]) == []
    assert method_8([1]) == [1]


# def test_method_9_removes_duplicates_using_itertools():
#     assert method_9([1, 2, 2, 3, 3, 3]) == [1, 2, 3]
#     assert method_9([3, 2, 2, 1, 1, 1]) == [1, 2, 3]
#     assert method_9([]) == []
#     assert method_9([1]) == [1]


def test_method_10_removes_duplicates_using_ordereddict():
    assert method_10([1, 2, 2, 3, 3, 3]) == [1, 2, 3]
    assert method_10([3, 2, 2, 1, 1, 1]) == [3, 2, 1]
    assert method_10([]) == []
    assert method_10([1]) == [1]


if __name__ == "__main__":
    print(__doc__)
