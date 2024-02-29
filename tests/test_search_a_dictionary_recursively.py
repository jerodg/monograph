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
from search_a_dictionary_recursively.solution import method_0, method_1


# fixme: some issues here
def test_method_0_finds_key_in_flat_dictionary():
    dictionary = {'key1': 'value1', 'key2': 'value2'}
    assert method_0(dictionary, 'key1') == 'value1'


def test_method_0_returns_none_if_key_not_found():
    dictionary = {'key1': 'value1', 'key2': 'value2'}
    assert method_0(dictionary, 'key3') is None


def test_method_0_finds_key_in_nested_dictionary():
    dictionary = {'key1': 'value1', 'key2': {'key3': 'value3'}}
    assert method_0(dictionary, 'key3') == 'value3'


def test_method_1_yields_all_occurrences_of_key():
    dictionary = {'key1': 'value1', 'key2': {'key1': 'value2'}}
    assert list(method_1(dictionary, 'key1')) == ['value1', 'value2']


def test_method_1_yields_nothing_if_key_not_found():
    dictionary = {'key1': 'value1', 'key2': {'key1': 'value2'}}
    assert list(method_1(dictionary, 'key3')) == []


if __name__ == '__main__':
    print(__doc__)
