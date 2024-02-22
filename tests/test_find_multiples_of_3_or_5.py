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
from python_monograph.find_multiples_of_3_or_5.solution import (method_0, method_1, method_2, method_3, method_4, method_5,
                                                                method_6, method_7, method_8, method_9, method_10, method_11)

def test_method_0_returns_correct_sum():
    assert method_0() == 233168

def test_method_1_returns_correct_sum():
    assert method_1() == 233168

# fixme: this test is failing
def test_method_2_returns_correct_sum():
    assert method_2() == 233168

def method_3_returns_correct_sum():
    assert method_3() == 233168

def method_4_returns_correct_sum():
    assert method_4() == 233168

def method_5_returns_correct_sum():
    assert method_5() == 233168

def method_6_returns_correct_sum():
    assert method_6() == 233168

def method_7_returns_correct_sum():
    assert method_7() == 233168

def method_8_returns_correct_sum():
    assert method_8() == 233168

def method_9_returns_correct_sum():
    assert method_9() == 233168

def method_10_returns_correct_sum():
    assert method_10() == 233168

def method_11_returns_correct_sum():
    assert method_11() == 233168

def test_method_0_with_no_multiples():
    assert method_0(1) == 0

def test_method_1_with_no_multiples():
    assert method_1(1) == 0

def test_method_2_with_no_multiples():
    assert method_2(1) == 0

def method_3_with_no_multiples():
    assert method_3(1) == 0

def method_4_with_no_multiples():
    assert method_4(1) == 0

def method_5_with_no_multiples():
    assert method_5(1) == 0

def method_6_with_no_multiples():
    assert method_6(1) == 0

def method_7_with_no_multiples():
    assert method_7(1) == 0

def method_8_with_no_multiples():
    assert method_8(1) == 0

def method_9_with_no_multiples():
    assert method_9(1) == 0

def method_10_with_no_multiples():
    assert method_10(1) == 0

def method_11_with_no_multiples():
    assert method_11(1) == 0

if __name__ == "__main__":
    print(__doc__)
