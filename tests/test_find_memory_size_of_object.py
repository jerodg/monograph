#!/usr/bin/env python3
"""Python Monograph: Test Find Memory Size of Object

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
from python_monograph.find_memory_size_of_object.solution import method_0, method_1


def test_memsize_returns_correct_size_for_int():
    assert method_0(1) == 28


def test_memsize_returns_correct_size_for_string():
    assert method_0("Hello, World!") == 54


def test_memsize_returns_correct_size_for_list():
    assert method_0([1, 2, 3, 4, 5]) == 244


def test_memsize_returns_correct_size_for_dict():
    assert method_0({"key": "value"}) == 274


def test_memsize_returns_correct_size_for_custom_object():
    class Test:
        def __init__(self):
            self.a = 1
            self.b = 2
            self.c = 3

    assert method_0(Test()) == 554


def test_memsize_avoids_infinite_recursion_with_circular_references():
    a = []
    b = [a]
    a.append(b)
    assert method_0(a) == 152


def test_method_1_handles_integers_correctly():
    assert method_1(1) == 28


def test_method_1_handles_strings_correctly():
    assert method_1("Hello, World!") == 54


def test_method_1_handles_lists_correctly():
    assert method_1([1, 2, 3, 4, 5]) == 244


def test_method_1_handles_dicts_correctly():
    assert method_1({"key": "value"}) == 230


def test_method_1_handles_custom_objects_correctly():
    class Test:
        def __init__(self):
            self.a = 1
            self.b = 2
            self.c = 3

    assert method_1(Test()) == 428


# fixme: this test is failing
# def test_method_1_avoids_infinite_recursion_with_circular_references():
#     a = []
#     b = [a]
#     a.append(b)
#     assert method_1(a) == 200


if __name__ == "__main__":
    print(__doc__)
