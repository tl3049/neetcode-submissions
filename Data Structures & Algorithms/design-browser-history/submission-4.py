class LinkNode:
    def __init__(self, url = None, prev = None, next = None):
        self.url = url
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.state = LinkNode(homepage)


    def visit(self, url: str) -> None:
        node = LinkNode(url)
        self.state.next = node
        node.prev = self.state

        self.state = node

    def back(self, steps: int) -> str:
        cur = self.state
        while cur.prev and steps:
            cur = cur.prev
            steps -= 1
        self.state = cur
        return cur.url 

    def forward(self, steps: int) -> str:
        cur = self.state
        while cur.next and steps:
            cur = cur.next
            steps -= 1
        self.state = cur
        return cur.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)