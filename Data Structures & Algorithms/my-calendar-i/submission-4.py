# #INTERVAL SOLUTION
# class MyCalendar:
    
#     def __init__(self):
#         self.bookings = []

#     def book(self, startTime: int, endTime: int) -> bool:
#         for s, e in self.bookings:
#             if endTime <= s or startTime >= e:
#                 continue
#             else:
#                 return False
#         self.bookings.append([startTime, endTime])
#         return True

#SEGMENTTREE SOLUTION
class Tree:
    def __init__(self, L, R):
        self.L = L
        self.R = R
        self.left = None
        self.right = None
    def insert(self, l, r):
        if not self:
            return Tree(l, r)
        if r <= self.L:
            if not self.left:
                self.left = Tree(l, r)
                return True
            if self.left.insert(l, r):
                return True
        elif l >= self.R:
            if not self.right:
                self.right = Tree(l, r)
                return True
            if self.right.insert(l, r):
                return True
        else:
            return False


class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.root:
            self.root = Tree(startTime, endTime)
            return True
        else:
            return True if self.root.insert(startTime, endTime) else False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)