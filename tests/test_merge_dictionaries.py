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

from src.python_monograph import (
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
    method_9,
)


def test_method_0_merges_dictionaries_correctly():
    assert method_0({'a': 1}, {'b': 2}) == {'a': 1, 'b': 2}


def test_method_0_overwrites_duplicate_keys():
    assert method_0({'a': 1}, {'a': 2}) == {'a': 2}


def test_method_1_merges_dictionaries_correctly():
    assert method_1({'a': 1}, {'b': 2}) == {'a': 1, 'b': 2}


def test_method_1_overwrites_duplicate_keys():
    assert method_1({'a': 1}, {'a': 2}) == {'a': 2}


def test_method_2_merges_dictionaries_correctly():
    assert method_2({'a': 1}, {'b': 2}) == {'a': 1, 'b': 2}


def test_method_2_overwrites_duplicate_keys():
    assert method_2({'a': 1}, {'a': 2}) == {'a': 2}


def test_method_3_merges_dictionaries_correctly():
    assert method_3({'a': 1}, {'b': 2}) == {'a': 1, 'b': 2}


def test_method_3_overwrites_duplicate_keys():
    assert method_3({'a': 1}, {'a': 2}) == {'a': 2}


def test_method_4_merges_dictionaries_correctly():
    assert method_4({'a': 1}, {'b': 2}) == {'a': 1, 'b': 2}


def test_method_4_overwrites_duplicate_keys():
    assert method_4({'a': 1}, {'a': 2}) == {'a': 2}


def test_method_5_merges_dictionaries_correctly():
    assert method_5({'a': 1}, {'b': 2}) == {'a': 1, 'b': 2}


def test_method_5_overwrites_duplicate_keys():
    assert method_5({'a': 1}, {'a': 2}) == {'a': 2}


def test_method_6_merges_dictionaries_correctly():
    assert method_6({'a': 1}, {'b': 2}) == {'a': 1, 'b': 2}


def test_method_6_overwrites_duplicate_keys():
    assert method_6({'a': 1}, {'a': 2}) == {'a': 2}


def test_method_7_merges_dictionaries_correctly():
    assert method_7({'a': 1}, {'b': 2}) == {'a': 1, 'b': 2}


def test_method_7_overwrites_duplicate_keys():
    assert method_7({'a': 1}, {'a': 2}) == {'a': 2}


def test_method_8_merges_dictionaries_correctly():
    assert method_8({'a': 1}, {'b': 2}) == {'a': 1, 'b': 2}


def test_method_8_overwrites_duplicate_keys():
    assert method_8({'a': 1}, {'a': 2}) == {'a': 2}


def test_method_9_merges_dictionaries_correctly():
    assert method_9({'a': 1}, {'b': 2}) == {'a': 1, 'b': 2}


def test_method_9_overwrites_duplicate_keys():
    assert method_9({'a': 1}, {'a': 2}) == {'a': 2}


def test_method_10_merges_dictionaries_correctly():
    assert method_10({'a': 1}, {'b': 2}) == {'a': [1], 'b': [2]}


def test_method_10_merges_duplicate_keys():
    assert method_10({'a': 1}, {'a': 2}) == {'a': [1, 2]}


if __name__ == '__main__':
    print(__doc__)
