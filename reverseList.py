# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # # Iterative
        # prev = None
        # while head:
        #     curr = head
        #     head = head.next
        #     curr.next = prev
        #     prev = curr
        # return prev

        # Recursive
        if head == None or head.next == None:
            return head
        prev = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return prev
