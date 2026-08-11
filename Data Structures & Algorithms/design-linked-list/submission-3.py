class LinkNode:
    def __init__(self, val, prev_node = None, next_node = None):
        self.val = val
        self.prev = prev_node
        self.next = next_node

class MyLinkedList:

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length: 
            return -1
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        if self.head:#not empty
            node = LinkNode(val)
            self.head.prev = node
            node.next = self.head
            self.head = node
        else:#head is empty: initilize head and tail node
            node = LinkNode(val)
            self.head = node
            self.tail = node
        self.length += 1 #length + 1

    def addAtTail(self, val: int) -> None:
        if self.tail:#not empty
            node = LinkNode(val)
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:#empty: initilize head and tail node
            node = LinkNode(val)
            self.head = node
            self.tail = node
        self.length += 1 #length + 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < self.length:
            cur = self.head
            for i in range(index):
                cur = cur.next
            #assign pointers
            new_node = LinkNode(val)
            pre_node = cur.prev
            next_node = cur
            #form new strings
            new_node.next = cur
            new_node.prev = pre_node
            pre_node.next = new_node
            cur.prev = new_node
            
            self.length += 1
        elif index == self.length:
            self.addAtTail(val)
        else:
            pass
    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self.length: 
            if index == 0:
                if self.length == 1:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif self.length > 1 and index == self.length - 1:
                prev_node = self.tail.prev
                prev_node.next = None
                self.tail = prev_node
            else:
                cur = self.head
                for i in range(index):
                    cur = cur.next
                prev_node = cur.prev
                next_node = cur.next
                prev_node.next = next_node
                next_node.prev = prev_node
            self.length -= 1
        else:
            pass

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)