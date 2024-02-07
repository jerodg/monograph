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

import pytest
from python_monograph.check_if_a_substring_is_in_a_list_strings.solution import method_0, method_1, method_2, method_3, method_4, method_5

def test_substring_present_in_list_using_any():
    assert method_0(["Hello", "World"], "World") == True

def test_substring_not_present_in_list_using_any():
    assert method_0(["Hello", "World"], "Python") == False

def test_substring_present_in_list_using_find():
    assert method_1(["Hello", "World"], "World") == True

def test_substring_not_present_in_list_using_find():
    assert method_1(["Hello", "World"], "Python") == False

def test_substring_present_in_list_using_find_list_comprehension():
    assert method_2(["Hello", "World"], "World") == True

def test_substring_not_present_in_list_using_find_list_comprehension():
    assert method_2(["Hello", "World"], "Python") == False

def test_substring_present_in_list_using_join():
    assert method_3(["Hello", "World"], "World") == True

def test_substring_not_present_in_list_using_join():
    assert method_3(["Hello", "World"], "Python") == False

def test_substring_present_in_list_using_for_loop():
    assert method_4(["Hello", "World"], "World") == True

def test_substring_not_present_in_list_using_for_loop():
    assert method_4(["Hello", "World"], "Python") == False

def test_substring_present_in_list_using_list_comprehension():
    assert method_5(["Hello", "World"], "World") == True

def test_substring_not_present_in_list_using_list_comprehension():
    assert method_5(["Hello", "World"], "Python") == False
