# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        order = 1
        n1 = n2 = 0
        while l1:
            n1 += l1.val * order
            order *= 10
            l1 = l1.next
        order = 1
        while l2:
            n2 += l2.val * order
            order *= 10
            l2 = l2.next
        sum_n = n1 + n2
        dummy = sum_node = ListNode()
        if sum_n == 0:
            return sum_node
        while sum_n > 0:
            mod = sum_n % 10
            sum_n //= 10
            sum_node.next = ListNode(mod)
            sum_node = sum_node.next
        return dummy.next
