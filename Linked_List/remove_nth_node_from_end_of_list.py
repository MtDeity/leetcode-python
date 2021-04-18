from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> Optional[ListNode]:
        left = right = head
        for _ in range(n):
            if not right:
                raise IndexError
            right = right.next
        if not right:
            return head.next
        while right.next:
            if not left.next:
                raise TypeError
            left = left.next
            right = right.next
        if not left.next:
            raise TypeError
        left.next = left.next.next
        return head
