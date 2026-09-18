class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        #DFS solution + cache
        cache = [[-1] * (capacity + 1) for _ in range(len(profit))]
        def dfs(i, cap):
            if i == len(profit):
                return 0
            if cache[i][cap] != -1:
                return cache[i][cap]
            maxProfit = dfs(i+1, cap) 
            nCap = cap - weight[i]
            if nCap >= 0:
                choose = profit[i] + dfs(i + 1, nCap)
                maxProfit = max(maxProfit, choose)
            cache[i][cap] = maxProfit
            return maxProfit
        return dfs(0, capacity)