class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        st_color = image[sr][sc]
        if st_color == color:
            return image
        ROWS, COLS = len(image), len(image[0])
        record = set()
        def dfs(i, j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS:
                return
            if image[i][j] != st_color:
                return
            if (i,j) in record:
                return
            record.add((i, j))
            image[i][j] = color

            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
            
            return

        dfs(sr, sc)
        return image
