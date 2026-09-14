#INTERVAL SOLUTION
class MyCalendar:
    
    def __init__(self):
        self.bookings = []

    def book(self, startTime: int, endTime: int) -> bool:
        for s, e in self.bookings:
            if endTime <= s or startTime >= e:
                continue
            else:
                return False
        self.bookings.append([startTime, endTime])
        return True



# class MyCalendar:
    
#     def __init__(self):
        

#     def book(self, startTime: int, endTime: int) -> bool:

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)