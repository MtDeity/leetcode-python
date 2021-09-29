from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self,
                         head: Optional[ListNode],
                         k: int) -> list[Optional[ListNode]]:
        parts: list[Optional[ListNode]] = []
        n = 0
        cur = head
        while cur:
            cur = cur.next
            n += 1
        quotient = n // k
        remainder = n % k
        cur = head
        for i in range(k):
            parts.append(cur)
            for _ in range(quotient - 1 + (i < remainder)):
                cur = cur.next
            if cur:
                cur.next, cur = None, cur.next
        return parts
