#!/usr/bin/env python3
"""Python Monograph: Check if a Substring is in a List of Strings Solution 01

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
from typing import List


def solution_01(data: List[str], substr: str) -> bool:
    """This function checks if a given substring is found in any of the strings in a list using the find() method.

    The find() method returns the lowest (first) index in the string where the substring is found within the slice.
    If the substring is not found, the find() method returns -1.

    Parameters:
        data (List[str]): A list of strings where the substring will be searched.
        substr (str): The substring to search in the list of strings.

    Returns:
        bool: True if the substring is found in any string in the list, False otherwise.

    Note:
        This function does not provide the location of the substring in the string.

    Example:
    >>> solution_01(["apple", "banana", "cherry"], "app")
    True
    >>> solution_01(["apple", "banana", "cherry"], "z")
    False

    References:
        https://docs.python.org/3/library/stdtypes.html?highlight=find#str.find
    """
    for row in data:
        if row.find(substr) != -1:  # Returns -1 if not found
            return True

    return False


if __name__ == "__main__":
    print(__doc__)
