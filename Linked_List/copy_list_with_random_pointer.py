# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head

        current = head
        while current:
            current.next = Node(current.val, current.next, current.random)
            current = current.next.next

        current = head
        while current:
            if current.random and current.next.next:
                current.next.random, current.next.next, current = current.random.next, current.next.next.next, current.next.next
            elif current.random:
                current.next.random, current = current.random.next, current.next.next
            elif current.next.next:
                current.next.next, current = current.next.next.next, current.next.next,
            else:
                current = current.next.next

        return head.next
