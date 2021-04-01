from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev: Optional[ListNode] = None
        slow: Optional[ListNode] = head
        fast: Optional[ListNode] = head
        while slow and fast and fast.next:
            fast = fast.next.next
            slow, rev, rev.next = slow.next, slow, rev
        if slow and fast:
            slow = slow.next
        while slow and rev and slow.val == rev.val:
            slow = slow.next
            rev = rev.next
        return not rev
