class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #dp with optimal space complexity
        # m, n = len(obstacleGrid), len(obstacleGrid[0])
        # pre = [0] * (n+1)
        # cur = [0] * (n+1)
        # if obstacleGrid[m - 1][n - 1] == 1:
        #     return 0
        # for row in range(m - 1, -1, -1):
        #     cur = [0] * (n+1)
        #     for col in range(n - 1, -1, -1):
        #         if row == m - 1 and col == n - 1:
        #             cur[n - 1] = 1
        #             continue
        #         if obstacleGrid[row][col] == 0:
        #             cur[col] = pre[col] + cur[col + 1]
        #     pre = cur
        # return cur[0]
    
        
        
        
        
        
        
        
        
        
        
        
        #dp with arrays
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        if obstacleGrid[m-1][n-1] == 0:
            dp[m - 1][n - 1] = 1
        else:
            return 0
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if row == m - 1 and col == n - 1:
                    continue
                if obstacleGrid[row][col] == 0:
                    dp[row][col] += dp[row][col + 1] + dp[row + 1][col]
        return dp[0][0]























        #memoization
        # m, n = len(obstacleGrid), len(obstacleGrid[0])
        # memo = {}
        # def dfs(i, j, m, n):
        #     if i == m - 1 and j == n - 1:
        #         if obstacleGrid[i][j] == 0:
        #             return 1
        #         else:
        #             return 0
        #     if i >= m or j >= n or obstacleGrid[i][j] == 1:
        #         return 0
        #     if (i, j) in memo:
        #         return memo[(i, j)]
        #     memo[(i, j)] = dfs(i + 1, j, m, n) + dfs(i, j + 1, m, n)
        #     return memo[(i, j)]
        # return dfs(0, 0, m, n)