class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.array = [0] * capacity
    def get(self, i: int) -> int:
        if i < self.length and i >= 0:
            return self.array[i]

    def set(self, i: int, n: int) -> None:
        if i < self.length and i >= 0:
            self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.array[self.length] = n
        self.length += 1

    def popback(self) -> int:
        if self.length != 0:
            self.length -= 1
            return self.array[self.length] 

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        narray = [0] * self.capacity
        for i in range(self.length):
            narray[i] = self.array[i]
        self.array = narray

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity