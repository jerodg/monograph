#!/usr/bin/env python3
"""Python Monograph: Natural Sort

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
from re import compile, split

DRE = compile(r"(\d+)")


def method_0(x: list, rvrs: bool = False) -> list:
    if isinstance(x, list):
        return [
            method_0(y, rvrs=rvrs)
            for y in sorted(
                x,
                key=lambda _: [int(s) if s.isdigit() else s.lower() for s in split(DRE, _)],
                reverse=rvrs,
            )
        ]


if __name__ == "__main__":
    print(__doc__)
