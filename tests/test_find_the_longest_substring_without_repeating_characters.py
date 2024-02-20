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
from python_monograph.find_the_longest_substring_without_repeating_characters.solution import method_0


def test_method_0_with_empty_string():
    assert method_0("") == (0, "")


def test_method_0_with_single_character():
    assert method_0("a") == (1, "a")


def test_method_0_with_repeated_character():
    assert method_0("aa") == (1, "a")


def test_method_0_with_two_different_characters():
    assert method_0("ab") == (2, "ab")


def test_method_0_with_non_overlapping_substrings():
    assert method_0("abcabc") == (3, "abc")


# fixme: the function provides the last substring instead of the first
def test_method_0_with_overlapping_substrings():
    assert method_0("abcba") == (3, "cba")


def test_method_0_with_all_unique_characters():
    assert method_0("abcdef") == (6, "abcdef")


def test_method_0_with_all_same_characters():
    assert method_0("aaaaaa") == (1, "a")


if __name__ == "__main__":
    print(__doc__)
