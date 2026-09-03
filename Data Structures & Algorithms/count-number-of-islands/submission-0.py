class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r, c = len(grid), len(grid[0])
        record = set()
        num = 0

        def dfs(i, j):
            if i < 0 or i >= r or j < 0 or j >= c:
                return
            if grid[i][j] == "0":
                return
            if (i, j) in record:
                return
            record.add((i,j))
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
            return
        
        
        for m in range(0, r):
            for n in range(0, c):
                if grid[m][n] == "1" and (m, n) not in record:
                    num += 1
                    dfs(m, n)
        return num