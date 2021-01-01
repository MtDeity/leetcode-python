from __future__ import annotations


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: ListNode = None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        odd: ListNode = head
        even: ListNode = head.next
        even_head: ListNode = head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head

        return head


assert ListNode.add.__annotations__ == {
    'next': 'ListNode'
}
