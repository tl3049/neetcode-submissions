from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        q.append((0,0))
        visited.add((0,0))
        length = 1
        directions = [[-1, -1], [-1, 0], [-1, 1], 
        [0, -1], [0, 1], [1, -1], [1, 0],[1, 1]]
        while q:
            n = len(q)#size of current layer
            for i in range(n):
                row, col = q.popleft()
                if row == ROWS - 1 and col == COLS - 1:
                    return length
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or 
                        grid[nr][nc] == 1 or (nr, nc) in visited):
                        continue
                    q.append((nr, nc))
                    visited.add((nr, nc))
            length += 1
        return -1        