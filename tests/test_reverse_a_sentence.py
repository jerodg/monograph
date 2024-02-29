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
from reverse_a_sentence import method_0, method_1, method_2, method_3, method_4, method_5, method_6


def test_method_0_reverses_entire_sentence():
    assert method_0('Hello World') == 'dlroW olleH'
    assert method_0('') == ''
    assert method_0('a') == 'a'


def test_method_1_reverses_letters_of_each_word():
    assert method_1('Hello World') == 'olleH dlroW'
    assert method_1('') == ''
    assert method_1('a') == 'a'


def test_method_2_reverses_entire_sentence_using_slice():
    assert method_2('Hello World') == 'dlroW olleH'
    assert method_2('') == ''
    assert method_2('a') == 'a'


def test_method_3_reverses_entire_sentence_using_shorthand_slice():
    assert method_3('Hello World') == 'dlroW olleH'
    assert method_3('') == ''
    assert method_3('a') == 'a'


def test_method_4_changes_word_order_only():
    assert method_4('Hello World') == 'World Hello'
    assert method_4('') == ''
    assert method_4('a') == 'a'


def test_method_5_reverses_word_order():
    assert method_5('Hello World') == 'World Hello'
    assert method_5('') == ''
    assert method_5('a') == 'a'


def test_method_6_reverses_word_order_using_list_comprehension():
    assert method_6('Hello World') == 'World Hello'
    assert method_6('') == ''
    assert method_6('a') == 'a'


# fixme: this is broken
# def test_method_7_reverses_word_order_using_reduce():
#     assert method_7("Hello World") == "World Hello"
#     assert method_7("") == ""
#     assert method_7("a") == "a"

if __name__ == '__main__':
    print(__doc__)
