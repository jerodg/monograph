#!/usr/bin/env python3
"""Python Monograph: Test Find the Equilibrium Index of an Array

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
from find_the_equilibrium_index_of_an_array.solution import method_0, method_1


def test_method_0_equilibrium_index_found():
    arr = [-7, 1, 5, 2, -4, 3, 0]
    assert method_0(arr) == 3


def test_method_0_no_equilibrium_index():
    arr = [1, 2, 3, 4, 5]
    assert method_0(arr) == -1


def test_method_0_empty_array():
    arr = []
    assert method_0(arr) == -1


def test_method_1_equilibrium_index_found():
    arr = [-7, 1, 5, 2, -4, 3, 0]
    assert method_1(arr) == 3


def test_method_1_no_equilibrium_index():
    arr = [1, 2, 3, 4, 5]
    assert method_1(arr) == -1


def test_method_1_empty_array():
    arr = []
    assert method_1(arr) == -1


if __name__ == '__main__':
    print(__doc__)
