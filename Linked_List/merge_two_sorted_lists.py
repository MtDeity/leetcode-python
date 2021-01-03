# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # # iterative
        # dummy = merged = ListNode()
        # while l1 and l2:
        #     if l1.val < l2.val:
        #         merged.next = l1
        #         l1 = l1.next
        #     else:
        #         merged.next = l2
        #         l2 = l2.next
        #     merged = merged.next
        # merged.next = l1 or l2
        # return dummy.next

        # recursive
        if not l1 or not l2:
            return l1 or l2
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
