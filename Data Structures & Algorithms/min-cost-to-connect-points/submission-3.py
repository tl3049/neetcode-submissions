import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
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

        n = len(points)
        adj = {i:[] for i in range(n)}
        for i in range(n):
            xi, yi = points[i]
            for j in range(i + 1, n):
                xj, yj = points[j]
                weight = abs(xi - xj) + abs(yi - yj)
                adj[i].append([weight, j])
                adj[j].append([weight, i])
        minH = [[0, 0]]
        visit = set()
        total = 0
        while minH:
            w, dst = heapq.heappop(minH)
            if dst in visit:
                continue
            visit.add(dst)
            total += w
            if len(visit) == n:
                return total
            for weight, ndst in adj[dst]:
                if ndst not in visit:
                    heapq.heappush(minH, [weight, ndst])