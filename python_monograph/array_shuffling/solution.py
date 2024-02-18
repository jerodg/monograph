#!/usr/bin/env python3
"""Python Monograph: Array Shuffling

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


# fixme: these all need verification
def method_0(arr: list) -> list:
    """This function shuffles an array in a specific manner. It ensures that any elements at even indices are no larger than any elements at odd indices.

    Parameters:
    arr (list): The array to be shuffled.

    Returns:
    list: The shuffled array.

    Approach:
    1. Sort the array.
    2. Swap every two elements starting from the second element.
    """
    # Sort the array
    arr.sort()

    # Iterate over the array, starting from the second element (index 1)
    # Swap every two elements
    for i in range(1, len(arr) - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]

    # Return the shuffled array
    return arr


def method_1(arr: list) -> list:
    """This function shuffles an array in a specific manner. It ensures that any elements at even indices are no larger than any elements at odd indices.

    Parameters:
    arr (list): The array to be shuffled.

    Returns:
    list: The shuffled array.

    Approach:
    1. Sort the array.
    2. Create a new array and start filling it by taking the smallest element (first element) from the sorted array and then the largest element (last element).
    3. Continue this process until the original array is empty.
    """
    # Sort the array
    arr.sort()

    # Create a new array
    result = []

    # Start filling the new array by taking the smallest and largest elements from the sorted array
    while arr:
        result.append(arr.pop(0))
        if arr:
            result.append(arr.pop())

    # Return the shuffled array
    return result


def method_2(arr: list) -> list:
    arr.sort()
    e = len(arr) // 2

    odd = arr[: e + 1]
    evn = arr[e:]

    out = []
    for i in range(len(arr)):
        try:
            if i % 2:
                out.append(evn.pop())
            else:
                out.append(odd.pop())
        except:
            pass

    return out


if __name__ == "__main__":
    print(__doc__)
