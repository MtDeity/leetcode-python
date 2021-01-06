# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        current = head
        stack = []
        while current:
            if current.child:
                if current.next:
                    stack.append(current.next)
                current.next = current.child
                current.next.prev = current
                current.child = None
            elif not current.next:
                if not stack:
                    break
                top = stack.pop()
                current.next = top
                current.next.prev = current
            current = current.next
        return head
