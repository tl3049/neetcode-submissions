class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if self.stack and val > self.min_stack[-1]:
            self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(val)
        self.stack.append(val)
        
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()      

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.stack:
            return self.min_stack[-1]
