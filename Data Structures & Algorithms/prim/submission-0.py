import heapq
class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for i in range(n):
            adj[i] = []
        for src, dst, weight in edges:
            adj[src].append([weight, src, dst])
            adj[dst].append([weight, dst, src])
        minH = []
        for weight, src, dst in adj[0]:
            heapq.heappush(minH,[weight, src, dst])
        visit = set()
        visit.add(0)
        total = 0
        while minH:
            weight, src, dst = heapq.heappop(minH)
            if dst in visit:
                continue
            total += weight
            visit.add(dst)
            if len(visit) == n:
                return total
            for w, s, d in adj[dst]:
                if d not in visit:
                    heapq.heappush(minH, [w, s, d])
        return -1