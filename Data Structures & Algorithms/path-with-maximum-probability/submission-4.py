import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        probRes = {i:0 for i in range(n)}
        adj = {}
        for i in range(n):
            adj[i] = []
        for edge, prob in zip(edges, succProb):
            adj[edge[0]].append([edge[1], prob])
            adj[edge[1]].append([edge[0], prob])
        maxH = [[-1, start_node]]
        visit = set()
        while maxH:
            prob, src = heapq.heappop(maxH)
            if src not in visit:
                visit.add(src)
                probRes[src] = -prob
                if src == end_node:
                    break
            for d, p in adj[src]:
                if d in visit:
                    continue
                heapq.heappush(maxH, [p*prob, d])
        return probRes[end_node] 

