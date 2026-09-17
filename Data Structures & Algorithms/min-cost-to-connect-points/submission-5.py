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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #KRUSKAL'S ALGORITHM
        minH = []
        n = len(points)
        for i in range(n):
            xi, yi = points[i]
            for j in range(i + 1, n):
                xj, yj = points[j]
                weight = abs(xi - xj) + abs(yi - yj)
                heapq.heappush(minH, [weight, i, j])
        uf = UnionFind(n)
        total = 0
        k = 0
        while k < n - 1:
            weight, src, dst = heapq.heappop(minH)
            if not uf.union(src, dst):
                continue
            k += 1
            total += weight
        return total
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #PRIM'S ALGORITHM
        # adj = {}
        # n = len(points)
        # for i in range(n):
        #     adj[i] = []
        # for i in range(n):
        #     xi, yi = points[i]
        #     for j in range(n):
        #         if i != j:
        #             xj, yj = points[j]
        #             weight = abs(xi - xj) + abs(yi - yj)
        #             adj[i].append([weight, j])
        # minH = [[0, 0]]
        # visit = set()
        # total = 0
        # while minH:
        #     w, dst = heapq.heappop(minH)
        #     if dst in visit:
        #         continue
        #     visit.add(dst)
        #     total += w
        #     if len(visit) == n:
        #         return total
        #     for weight, ndst in adj[dst]:
        #         if ndst not in visit:
        #             heapq.heappush(minH, [weight, ndst])

        #FEWERS COMPUTATIONS PRIM'S ALGORITHM
        # n = len(points)
        # adj = {i:[] for i in range(n)}
        # for i in range(n):
        #     xi, yi = points[i]
        #     for j in range(i + 1, n):
        #         xj, yj = points[j]
        #         weight = abs(xi - xj) + abs(yi - yj)
        #         adj[i].append([weight, j])
        #         adj[j].append([weight, i])
        # minH = [[0, 0]]
        # visit = set()
        # total = 0
        # while minH:
        #     w, dst = heapq.heappop(minH)
        #     if dst in visit:
        #         continue
        #     visit.add(dst)
        #     total += w
        #     if len(visit) == n:
        #         return total
        #     for weight, ndst in adj[dst]:
        #         if ndst not in visit:
        #             heapq.heappush(minH, [weight, ndst])