from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # Iterative
        prev = None
        while head:
            current, head = head, head.next
            current.next, prev = prev, current
        return prev

        # # Recursive
        # if not head or not head.next:
        #     return head
        # prev = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return prev
