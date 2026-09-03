from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        #Use fresh to note all fresh fruits
        fresh = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        if not q:
            if fresh == 0:
                return 0
            else:
                return -1
                
        length = 0
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        while q and fresh > 0:
            n = len(q)
            for i in range(n):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (min(nr, nc) < 0 or nr >= ROWS or nc >= COLS 
                        or grid[nr][nc] != 1):
                        continue
                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    fresh -= 1
            length += 1
        return length if fresh == 0 else -1



        #put all rotten fruits positions into a queue
        # flag = 0
        # for i in range(ROWS):
        #     for j in range(COLS):
        #         if grid[i][j] == 2:
        #             q.append((i, j))
        #         if grid[i][j] == 1:
        #             flag = 1
        # if not q:
        #     if 1 == flag:
        #         return -1
        #     else:
        #         return 0

        # length = 0
        # directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        # while q:
        #     n = len(q)
        #     for i in range(n):
        #         r, c = q.popleft()
        #         for dr, dc in directions:
        #             nr, nc = r + dr, c + dc
        #             if (min(nr, nc) < 0 or nr >= ROWS or nc >= COLS 
        #                 or grid[nr][nc] != 1):
        #                 continue
        #             grid[nr][nc] = 2
        #             q.append((nr, nc))
        #     length += 1
        # for i in range(ROWS):
        #     for j in range(COLS):
        #         if grid[i][j] == 1:
        #             return -1
        # return length - 1
        