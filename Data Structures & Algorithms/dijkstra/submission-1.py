import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {}
        for i in range(n):
            adj[i] = []
        for s, d, w in edges:
            adj[s].append((d, w))
        
        shortest = {}
        minHeap = [(0, src)]
        while minHeap:
            c, s = heapq.heappop(minHeap)
            if s in shortest:
                continue
            shortest[s] = c
            for d, w in adj[s]:
                if d not in shortest:
                    heapq.heappush(minHeap, (c + w, d))
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        return shortest