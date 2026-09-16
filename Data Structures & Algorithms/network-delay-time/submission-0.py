import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []
        for u, v, t in times:
            adj[u].append([v, t])
        shortest = {}
        minHeap = [(0, k)]
        while minHeap:
            cost, src = heapq.heappop(minHeap)
            if src in shortest:
                continue
            shortest[src] = cost
            for v, t in adj[src]:
                if v not in shortest:
                    heapq.heappush(minHeap, (t + cost, v))
        res = -1
        for i in range(1, n + 1):
            if i in shortest:
                res = max(res, shortest[i])
            else:
                return -1
        return res