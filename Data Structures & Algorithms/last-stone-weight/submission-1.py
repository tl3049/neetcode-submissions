import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        stones = [-val for val in stones]
        heapq.heapify(stones)
        while len(stones) > 2:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x == y:
                continue
            else:
                heapq.heappush(stones, -abs(x - y))
            print(stones)
        if len(stones) == 1:
            return -stones[0]
        else:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            return abs(x - y)