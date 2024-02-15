#!/usr/bin/env python3
"""Python Monograph: Calculate Size Automatically

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


def convert_bytes(size, notation: str = "decimal") -> str:
    """Convert Bytes

    :param size:
    :type size:
    :param notation:
    :type notation:
    :return:
    :rtype:

    References:
        https://blog.codinghorror.com/gigabyte-decimal-vs-binary/
        https://physics.nist.gov/cuu/Units/binary.html
        https://ux.stackexchange.com/questions/13815/files-size-units-kib-vs-kb-vs-kb
    """
    if size < 0:
        raise ValueError("Size cannot be negative.")

    if notation == "decimal":
        suffixes = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]
        base = 1000
    elif notation == "binary":
        suffixes = ["B", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YiB"]
        base = 1024
    else:
        raise ValueError("Invalid notation. Please choose 'decimal' or 'binary'.")

    index = 0
    while abs(size) >= base and index < len(suffixes) - 1:
        size /= base
        index += 1

    return f"{size:3.2f} {suffixes[index]}"


if __name__ == "__main__":
    print(__doc__)
