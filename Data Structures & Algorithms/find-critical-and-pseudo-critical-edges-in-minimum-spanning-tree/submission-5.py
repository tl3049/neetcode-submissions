class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
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
        if self.par[p1] >= self.par[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.par[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.par[p1]
        return True
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        minH = []
        E = len(edges)
        for i, edge in enumerate(edges):
            src, dst, weight = edge
            minH.append([weight, i, src, dst])
        minH.sort()
        uf = UnionFind(n)
        mst = 0
        critical, pseudo = [], []
        for i in range(E):
            weight, _, src, dst = minH[i]
            if not uf.union(src, dst):
                continue
            mst += weight
        for i, edge_i in enumerate(edges):
            #FIND CRITICAL EDGES
            total = 0
            uf = UnionFind(n)
            for j in range(E):
                weight, index, src, dst = minH[j]
                if index == i:
                    continue
                if not uf.union(src, dst):
                    continue
                total += weight
            if total != mst or max(uf.rank) < n:
                critical.append(i)
                continue
            
            #FIND PSEUDO CRITICAL EDGES
            uf = UnionFind(n)
            src, dst, total = edge_i
            uf.union(src, dst)
            for j in range(E):
                weight, index, src, dst = minH[j]
                if index == i:
                    continue
                if not uf.union(src, dst):
                    continue
                total += weight
            if total == mst:
                pseudo.append(i)
        return [critical, pseudo]
            
            




