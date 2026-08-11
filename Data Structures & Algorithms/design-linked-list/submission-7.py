class LinkNode:
    def __init__(self, val = 0, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:

    def __init__(self):
        #Length of the link
        self.length = 0
        #Two dummy nodes: left<-->Nodes<-->right
        self.left = LinkNode()
        self.right = LinkNode()
        #Connect the two nodes
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        if index < 0 or index > self.length - 1:
            return -1
        cur = self.left
        for _ in range(index + 1):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.length, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return -1
        cur = self.left
        for _ in range(index):
            cur = cur.next
        
        prev_node = cur
        node = LinkNode(val)
        next_node = cur.next
        
        prev_node.next = node
        
        node.prev = prev_node
        node.next = next_node

        next_node.prev = node
        
        self.length += 1


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.length - 1:
            return -1

        cur = self.left
        for _ in range(index):
            cur = cur.next
        
        prev_node = cur
        next_node = cur.next.next

        prev_node.next = next_node
        next_node.prev = prev_node

        self.length -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)