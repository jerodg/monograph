#!/usr/bin/env python3
"""Python Monograph: Find Unique Keys from a List of Dicts

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
import pytest

from python_monograph.find_unique_keys_from_a_list_of_dicts.solution import method_0, method_1, method_2, method_3


@pytest.fixture
def list_of_dicts():
    return [{"a": 1, "b": 2}, {"b": 3, "c": 4}, {"c": 5, "d": 6}]


def test_unique_keys_using_chain_itertools(list_of_dicts):
    assert set(method_0(list_of_dicts)) == {"a", "b", "c", "d"}


def test_unique_keys_using_list_dict_comprehension(list_of_dicts):
    assert set(method_1(list_of_dicts)) == {"a", "b", "c", "d"}


def test_unique_keys_using_keys_extend_list_set_methods(list_of_dicts):
    assert set(method_2(list_of_dicts)) == {"a", "b", "c", "d"}


def test_unique_keys_using_functools_reduce(list_of_dicts):
    assert set(method_3(list_of_dicts)) == {"a", "b", "c", "d"}


def test_empty_list_input():
    assert method_0([]) == []


def test_single_dict_input():
    assert set(method_0([{"a": 1, "b": 2}])) == {"a", "b"}


def test_no_common_keys_input():
    assert set(method_0([{"a": 1}, {"b": 2}, {"c": 3}])) == {"a", "b", "c"}


if __name__ == "__main__":
    print(__doc__)
