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
        # #ITERATIVE FORM
        # cur = self
        # while True:
        #     if r <= cur.L:
        #         if not cur.left:
        #             cur.left = Tree(l, r)
        #             return True
        #         cur = cur.left
        #     elif l >= cur.R:
        #         if not cur.right:
        #             cur.right = Tree(l, r)
        #             return True
        #         cur = cur.right
        #     else:
        #         return False
        #RECURSION FORM
        if r <= self.L:
            if not self.left:
                self.left = Tree(l, r)
                return True
            return self.left.insert(l, r)
        elif l >= self.R:
            if not self.right:
                self.right = Tree(l, r)
                return True
            return self.right.insert(l, r)
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