# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        reversed_node: ListNode = None
        slow: ListNode = head
        fast: ListNode = head
        while fast and fast.next:
            fast = fast.next.next
            slow, reversed_node, reversed_node.next = slow.next, slow, reversed_node
        if fast:
            slow = slow.next
        while reversed_node and slow.val == reversed_node.val:
            slow = slow.next
            reversed_node = reversed_node.next
        return not reversed_node
