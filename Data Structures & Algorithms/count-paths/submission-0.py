class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #memo
        memo = {}
        def dfs(i, j, m, n):
            if i >= m or j >= n:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            if (i, j) in memo:
                return memo[(i, j)]
            memo[(i, j)] = dfs(i+1, j, m, n) + dfs(i, j + 1, m, n)
            return memo[(i, j)]
        return dfs(0, 0, m, n)
