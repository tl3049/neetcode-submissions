class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        area = 0
        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return 0
            if grid[i][j] == 0:
                return 0
            if (i, j) in visit:
                return 0
            visit.add((i,j))
            return 1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    area = max(area, dfs(r, c))
        return area

