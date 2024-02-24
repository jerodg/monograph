#!/usr/bin/env python3
"""Python Monograph: Find the Longest Substring Without Repeating Characters Solution

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


def method_0(s: str) -> tuple[int, str]:
    """This function finds the longest substring without repeating characters in a given string.

    Parameters:
        s (str): The input string.

    Returns:
        tuple[int, str]: A tuple containing the length of the longest substring without repeating characters and the substring
        itself.
    """

    start = 0
    max_length = 0
    used_chars = {}

    for end in range(len(s)):
        if s[end] in used_chars and start <= used_chars[s[end]]:
            start = used_chars[s[end]] + 1
        else:
            max_length = max(max_length, end - start + 1)

        used_chars[s[end]] = end

    return max_length, s[start : start + max_length]


def method_1(s: str) -> tuple[int, str]:
    """This function finds the longest substring without repeating characters in a given string using a different approach.

    Parameters:
        s (str): The input string.

    Returns:
        tuple[int, str]: A tuple containing the length of the longest substring without repeating characters and the substring
        itself.
    """

    start = 0
    max_length = 0
    unique_chars = set()

    for end in range(len(s)):
        while s[end] in unique_chars:
            unique_chars.remove(s[start])
            start += 1
        unique_chars.add(s[end])
        max_length = max(max_length, end - start + 1)

    return max_length, s[start : start + max_length]


if __name__ == "__main__":
    print(__doc__)
