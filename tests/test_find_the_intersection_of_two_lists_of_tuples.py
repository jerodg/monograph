#!/usr/bin/env python3
"""Python Monograph: Test Find the Intersection of Two Lists of Tuples Solution

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
from python_monograph.find_the_intersection_of_two_lists_of_tuples.solution import method_0, method_1, method_2, method_3, method_4, method_5, method_6

def test_intersection_present_in_lists_using_sorted_set_and_list_comprehension():
    assert method_0([(1, 2), (3, 4)], [(3, 4), (5, 6)]) == [(3, 4)]

def test_intersection_not_present_in_lists_using_sorted_set_and_list_comprehension():
    assert method_0([(1, 2), (3, 4)], [(5, 6), (7, 8)]) == []

def test_intersection_present_in_lists_using_map_frozenset_and_and_operator():
    assert method_1([(1, 2), (3, 4)], [(3, 4), (5, 6)]) == [(3, 4)]

def test_intersection_not_present_in_lists_using_map_frozenset_and_and_operator():
    assert method_1([(1, 2), (3, 4)], [(5, 6), (7, 8)]) == set()

def test_intersection_present_in_lists_using_list_comprehension():
    assert method_2([(1, 2), (3, 4)], [(3, 4), (5, 6)]) == [(3, 4)]

def test_intersection_not_present_in_lists_using_list_comprehension():
    assert method_2([(1, 2), (3, 4)], [(5, 6), (7, 8)]) == []

def test_intersection_present_in_lists_using_set_intersection():
    assert method_3([(1, 2), (3, 4)], [(3, 4), (5, 6)]) == [(3, 4)]

def test_intersection_not_present_in_lists_using_set_intersection():
    assert method_3([(1, 2), (3, 4)], [(5, 6), (7, 8)]) == []

def test_intersection_present_in_lists_using_list_comprehension_with_in_operator():
    assert method_4([(1, 2), (3, 4)], [(3, 4), (5, 6)]) == [(3, 4)]

def test_intersection_not_present_in_lists_using_list_comprehension_with_in_operator():
    assert method_4([(1, 2), (3, 4)], [(5, 6), (7, 8)]) == []

def test_intersection_present_in_lists_using_filter_function():
    assert method_5([(1, 2), (3, 4)], [(3, 4), (5, 6)]) == [(3, 4)]

def test_intersection_not_present_in_lists_using_filter_function():
    assert method_5([(1, 2), (3, 4)], [(5, 6), (7, 8)]) == []

def test_intersection_present_in_lists_using_set_comprehension():
    assert method_6([(1, 2), (3, 4)], [(3, 4), (5, 6)]) == [(3, 4)]

def test_intersection_not_present_in_lists_using_set_comprehension():
    assert method_6([(1, 2), (3, 4)], [(5, 6), (7, 8)]) == []


if __name__ == "__main__":
    print(__doc__)
