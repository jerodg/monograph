#!/usr/bin/env python3
"""Python Monograph: Merge Two Sorted Lists Tests

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
from python_monograph.merge_two_sorted_lists.solution import ListNode, method_0, method_1, method_2


# todo: need better tests
def test_merge_two_sorted_lists_iterative():
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    result = method_0(l1, l2)
    assert result.val == 1
    assert result.next.val == 1
    assert result.next.next.val == 2
    assert result.next.next.next.val == 3
    assert result.next.next.next.next.val == 4
    assert result.next.next.next.next.next.val == 4

def test_merge_two_sorted_lists_recursive():
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    result = method_1(l1, l2)
    assert result.val == 1
    assert result.next.val == 1
    assert result.next.next.val == 2
    assert result.next.next.next.val == 3
    assert result.next.next.next.next.val == 4
    assert result.next.next.next.next.next.val == 4

def test_merge_two_sorted_lists_priority_queue():
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    result = method_2(l1, l2)
    assert result.val == 1
    assert result.next.val == 1
    assert result.next.next.val == 2
    assert result.next.next.next.val == 3
    assert result.next.next.next.next.val == 4
    assert result.next.next.next.next.next.val == 4

if __name__ == "__main__":
    print(__doc__)
