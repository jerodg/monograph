#!/usr/bin/env python3
"""Python Monograph: Check if a Substring is in a List of Strings Solution 01 Tests

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
from python_monograph.check_if_a_substring_is_in_a_list_strings.solution_01 import solution_01


def test_substring_present_in_list():
    assert solution_01(["apple", "banana", "cherry"], "app") == True


def test_substring_not_present_in_list():
    assert solution_01(["apple", "banana", "cherry"], "z") == False


def test_substring_present_in_empty_string():
    assert solution_01(["apple", "banana", "cherry", ""], "") == True


def test_substring_not_present_in_empty_list():
    assert solution_01([], "app") == False


def test_substring_case_sensitivity():
    assert solution_01(["apple", "banana", "cherry"], "APP") == False


def test_substring_in_list_with_special_characters():
    assert solution_01(["apple@", "#banana", "cherry!"], "@") == True
