#!/usr/bin/env python3
"""Python Monograph: Test Find Multiples of 3 and 5

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
from python_monograph.find_multiples_of_3_or_5.solution import method_0, method_1, method_2


def test_method_0_returns_correct_sum():
    assert method_0() == 233168


def test_method_1_returns_correct_sum():
    assert method_1() == 233168


def test_method_2_returns_correct_sum():
    assert method_2() == 233168


if __name__ == "__main__":
    print(__doc__)
