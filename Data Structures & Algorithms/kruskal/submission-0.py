class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}
        for i in range(n):
            self.par[i] = i
            self.rank[i] = 1
    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] +=1
        return True
import heapq
class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        minH = []
        for src, dst, weight in edges:
            heapq.heappush(minH, [weight, src, dst])
        uf = UnionFind(n)
        total = 0
        mst = []
        while minH:
            weight, src, dst = heapq.heappop(minH)
            if not uf.union(src, dst):
                continue
            total += weight
            mst.append([src, dst])
            if len(mst) == n - 1:
                return total
        return -1












