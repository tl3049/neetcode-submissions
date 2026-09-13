class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.maxSize = 1
    def find(self, n):
        p = self.parent[n]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] <= self.rank[p2]:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
            self.maxSize = max(self.maxSize, self.rank[p2])
        else:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
            self.maxSize = max(self.maxSize, self.rank[p1])
        #print(n1, n2, p1, p2, self.maxSize )
        return True

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        #UNION FIND SOLUTION
        numSet = set(nums)
        numToIndex = {}
        for num in nums:
            if num not in numToIndex:
                numToIndex[num] = len(numToIndex)
        #print(numToIndex)
        uf = DSU(len(numToIndex))
        for num in numSet:
            if num + 1 in numSet:
                #print(num)
                uf.union(numToIndex[num], numToIndex[num+1])
                #print(uf.maxSize)
        #print(uf.rank)
        return uf.maxSize


        # dic = Counter(nums)
        # res = 0
        # for num in nums:
        #     cur = num  
        #     if cur not in dic:
        #         continue
        #     dic.pop(num)
        #     count = 1
        #     while num + 1 in dic:
        #         dic.pop(num + 1)
        #         num = num + 1
        #         count += 1
        #     while cur - 1 in dic:
        #         dic.pop(cur - 1)
        #         cur -= 1
        #         count += 1
        #     res = max(res, count)
        # return res


        #ONE WHILE
        # numSet = set(nums)
        # res = 0
        # for num in numSet:
        #     if num - 1 not in numSet:#start from minimum
        #         length = 1  
        #         while length + num in numSet:
        #             length += 1
        #         res = max(res, length)
        # return res

