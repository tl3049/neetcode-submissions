import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfs = []
        minCaps = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(minCaps)
        for i in range(k):
            while minCaps and minCaps[0][0] <= w:
                c, p = heapq.heappop(minCaps)
                heapq.heappush(maxProfs, -1*p)
            if not maxProfs:
                break
            w += -1 * heapq.heappop(maxProfs)
        return w