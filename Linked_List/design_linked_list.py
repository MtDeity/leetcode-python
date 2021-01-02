class ListNode:
    def __init__(self, val: int = 0, prev: ListNode = None, next: ListNode = None):
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size or not self.head:
            return -1
        current = self.head
        for i in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        """
        list_node = ListNode(val)
        list_node.next = self.head
        if list_node.next:
            list_node.next.prev = list_node
        self.head = list_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        list_node = ListNode(val)
        current = self.head
        if not current:
            self.head = list_node
        else:
            while current.next:
                current = current.next
            current.next = list_node
            current.next.prev = current
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list,
        the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.size:
            return
        elif index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            current = self.head
            for i in range(1, index):
                current = current.next
            list_node = ListNode(val)
            list_node.next = current.next
            current.next = list_node
            current.next.next.prev = list_node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return
        elif index == 0:
            if self.head.next:
                self.head.next.prev = None
            self.head = self.head.next
        else:
            current = self.head
            for i in range(1, index):
                current = current.next
            current.next.prev = None
            current.next.next, current.next = None, current.next.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
