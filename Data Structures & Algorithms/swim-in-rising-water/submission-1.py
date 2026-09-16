import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #DIJKSTRA'S ALGORITHM
        N = len(grid)
        visit = set()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        minH = [[grid[0][0], 0, 0]]
        visit.add((0, 0))
        while minH:
            t, r, c = heapq.heappop(minH)

            if r == N - 1 and c == N - 1:
                return t

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if (nr < 0 or nc < 0 or nr >= N or nc >= N or
                    (nr, nc) in visit):
                    continue
                visit.add((nr, nc))
                heapq.heappush(minH, [max(grid[nr][nc], t), nr, nc])












            












        # WRONG CODE AND SHOULD BE CLARIFIED LATER
        # ROWS, COLS = len(grid), len(grid[0])
        # minTime = [[-1] * COLS for _ in range(ROWS)]
        # memo = {}
        # self.res = -1
        # visited = set()
        # directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        # def dfs(i, j):
        #     if i < 0 or j < 0 or i >= ROWS or j >= COLS:
        #         return max(ROWS*ROWS, COLS*COLS)
        #     if i == ROWS - 1 and j == COLS - 1:
        #         minTime[i][j] = grid[i][j]
        #         return grid[i][j]
        #     if (i, j) in memo:
        #         return memo[(i,j)]
        #     visited.add((i, j))
        #     tmp = max(ROWS*ROWS, COLS*COLS)
        #     for c, r in directions:
        #         val = max(grid[i][j], dfs(i + c, j + r))
        #         tmp = min(tmp, val)
        #     memo[(i, j)] = tmp
        #     visited.remove((i, j))
        #     return tmp
        # dfs(0, 0)
        # print(memo)
        # return self.res
        