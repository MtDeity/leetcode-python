# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head

        lgth = 1
        current = head
        while current.next:
            lgth += 1
            current = current.next
        current.next = head

        k = k % lgth
        current = head
        for i in range(lgth - k - 1):
            current = current.next
        new_head = current.next
        current.next = None

        return new_head
