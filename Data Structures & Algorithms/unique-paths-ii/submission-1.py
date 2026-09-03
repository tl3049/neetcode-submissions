class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        memo = {}
        def dfs(i, j, m, n):
            if i == m - 1 and j == n - 1:
                if obstacleGrid[i][j] == 0:
                    return 1
                else:
                    return 0
            if i >= m or j >= n or obstacleGrid[i][j] == 1:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            memo[(i, j)] = dfs(i + 1, j, m, n) + dfs(i, j + 1, m, n)
            return memo[(i, j)]
        return dfs(0, 0, m, n)