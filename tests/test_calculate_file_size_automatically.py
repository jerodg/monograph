#!/usr/bin/env python3
"""Python Monograph: Test Calculate File Size Automatically

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

from python_monograph.calculate_file_size_automatically.solution import convert_bytes


def test_convert_bytes_decimal_notation():
    assert convert_bytes(1500, 'decimal') == "1.50 KB"

def test_convert_bytes_binary_notation():
    assert convert_bytes(1500, 'binary') == "1.46 KiB"

def test_convert_bytes_large_size_decimal_notation():
    assert convert_bytes(1500000000, 'decimal') == "1.50 GB"

def test_convert_bytes_large_size_binary_notation():
    assert convert_bytes(1500000000, 'binary') == "1.40 GiB"

def test_convert_bytes_invalid_notation():
    with pytest.raises(ValueError):
        convert_bytes(1500, 'invalid')

def test_convert_bytes_negative_size():
    with pytest.raises(ValueError):
        convert_bytes(-1500, 'decimal')

def test_convert_bytes_zero_size():
    assert convert_bytes(0, 'decimal') == "0.00 B"
if __name__ == "__main__":
    print(__doc__)
