from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
            self,
            l1: Optional[ListNode],
            l2: Optional[ListNode]) -> Optional[ListNode]:
        # # Iterative
        # dummy = current = ListNode()
        # while l1 and l2:
        #     if l1.val <= l2.val:
        #         current.next = l1
        #         l1 = l1.next
        #     else:
        #         current.next = l2
        #         l2 = l2.next
        #     current = current.next
        # current.next = l1 or l2
        # return dummy.next

        # Recursive
        if not l1 or not l2:
            return l1 or l2
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
