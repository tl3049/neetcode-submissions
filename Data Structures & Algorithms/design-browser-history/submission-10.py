class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.i = 0
        self.n = 1

    def visit(self, url: str) -> None:
        if self.n == self.i + 1:
            self.history.append(url)
        else:
            self.history[self.i + 1] = url
        
        self.i += 1
        self.n = self.i + 1

    def back(self, steps: int) -> str:
        self.i = max(self.i - steps, 0)
        return self.history[self.i]

    def forward(self, steps: int) -> str:
        self.i = min(self.i + steps, self.n - 1)
        return self.history[self.i]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)