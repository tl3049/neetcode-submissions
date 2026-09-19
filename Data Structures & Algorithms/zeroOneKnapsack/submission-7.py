class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        #DP solution with one dimensional array
        # dp = [0] * (capacity + 1)
        # for i in range(capacity + 1):
        #     if i >= weight[0]:
        #         dp[i] = profit[0]
        # for i in range(1, len(profit)):
        #     for j in range(capacity, 0, -1):
        #         skip = dp[j]
        #         choose = 0
        #         if j >= weight[i]:
        #             choose = profit[i] + dp[j - weight[i]]
        #         dp[j] = max(skip, choose)
        # return dp[-1]

        #DP solution with two dimensional array
        # dp = [[0] * (capacity + 1) for _ in range(len(profit))]
        # for i in range(capacity + 1):
        #     if i >= weight[0]:
        #         dp[0][i] = profit[0]
        # for i in range(1, len(profit)):
        #     for j in range(1, capacity + 1):
        #         skip = dp[i - 1][j]
        #         choose = 0
        #         if j >= weight[i]:
        #             choose = profit[i] + dp[i - 1][j - weight[i]]
        #         dp[i][j] = max(skip, choose)
        # return dp[-1][-1]

        #DP solution with two dimensional array: fewer initialization
        # dp = [[0] * (capacity + 1) for _ in range(len(profit) + 1)]
        # for i in range(1, len(profit) + 1):
        #     for j in range(1, capacity + 1):
        #         skip = dp[i - 1][j]
        #         choose = 0
        #         if j >= weight[i - 1]:
        #             choose = profit[i - 1] + dp[i - 1][j - weight[i - 1]]
        #         dp[i][j] = max(skip, choose)
        # return dp[-1][-1]

         #DP solution with one dimensional array: fewer initialization
        dp = [0] * (capacity + 1)
        for i in range(1, len(profit) + 1):
            ndp = [0] * (capacity + 1)
            for j in range(1, capacity + 1):
                skip = dp[j]
                choose = 0
                if j >= weight[i - 1]:
                    choose = profit[i - 1] + dp[j - weight[i - 1]]
                ndp[j] = max(skip, choose)
            dp = ndp
        return dp[-1]

        ##DFS solution + cache
        # cache = [[-1] * (capacity + 1) for _ in range(len(profit))]
        # def dfs(i, cap):
        #     if i == len(profit):
        #         return 0
        #     if cache[i][cap] != -1:
        #         return cache[i][cap]
        #     maxProfit = dfs(i+1, cap) 
        #     nCap = cap - weight[i]
        #     if nCap >= 0:
        #         choose = profit[i] + dfs(i + 1, nCap)
        #         maxProfit = max(maxProfit, choose)
        #     cache[i][cap] = maxProfit
        #     return maxProfit
        # return dfs(0, capacity)