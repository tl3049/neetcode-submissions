class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #memo
        # memo = {}
        # def dfs(i, j, m, n):
        #     if i >= m or j >= n:
        #         return 0
        #     if i == m - 1 and j == n - 1:
        #         return 1
        #     if (i, j) in memo:
        #         return memo[(i, j)]
        #     memo[(i, j)] = dfs(i+1, j, m, n) + dfs(i, j + 1, m, n)
        #     return memo[(i, j)]
        # return dfs(0, 0, m, n)

        #dp with array
        # dp = [[0] * n for _ in range(m + 1)]
        # for row in range(m-1, -1, -1):
        #     dp[row][n-1] = 1
        #     for col in range(n-2, -1, -1):
        #         dp[row][col] = dp[row][col + 1] + dp[row + 1][col]
        # return dp[0][0]

        #dp with minimum space
        pre = [0] * n
        for row in range(m-1, -1, -1):
            cur = [0] * n
            cur[-1] = 1
            for col in range(n-2, -1, -1):
                cur[col] = cur[col + 1] + pre[col]
            pre = cur
        return cur[0]

