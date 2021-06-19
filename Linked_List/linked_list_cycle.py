from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next: Optional[ListNode] = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
