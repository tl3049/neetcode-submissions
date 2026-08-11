class LinkNode:
    def __init__(self, url = None, prev = None, next = None):
        self.url = url
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.state = LinkNode(homepage)#current state
        #Dummy nodes refering to the back and forward end
        self.left = LinkNode()
        self.right = LinkNode()        
        #Connect all the nodes
        self.state.next = self.right
        self.state.prev = self.left

        self.left.next = self.state
        self.right.prev = self.state

    def visit(self, url: str) -> None:
        node = LinkNode(url)
        self.state.next = node
        node.prev = self.state
        node.next = self.right
        self.state = node

    def back(self, steps: int) -> str:
        cur = self.state
        while cur.prev.url and steps:
            cur = cur.prev
            steps -= 1
        self.state = cur
        return cur.url 

    def forward(self, steps: int) -> str:
        cur = self.state
        while cur.next.url and steps:
            cur = cur.next
            steps -= 1
        self.state = cur
        return cur.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)