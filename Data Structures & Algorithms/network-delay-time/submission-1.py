import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []
        for u, v, t in times:
            adj[u].append([v, t])
        minHeap = [(0, k)]
        ##TWO PASS
        # shortest = {}
        # while minHeap:
        #     cost, src = heapq.heappop(minHeap)
        #     if src in shortest:
        #         continue
        #     shortest[src] = cost
        #     for v, t in adj[src]:
        #         if v not in shortest:
        #             heapq.heappush(minHeap, (t + cost, v))
        # res = -1
        # for i in range(1, n + 1):
        #     if i in shortest:
        #         res = max(res, shortest[i])
        #     else:
        #         return -1
        # return res

        #ONE PASS
        visited = set()
        res = -1
        while minHeap:
            cost, src = heapq.heappop(minHeap)
            if src in visited:
                continue
            visited.add(src)
            res = max(res, cost)
            for v, t in adj[src]:
                if v not in visited:
                    heapq.heappush(minHeap, (t + cost, v))
        return -1 if len(visited) != n else res
