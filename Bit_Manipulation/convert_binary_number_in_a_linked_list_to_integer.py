# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary = 0
        while head:
            binary = binary * 2 + head.val
            head = head.next
        return binary
