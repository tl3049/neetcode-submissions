class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.prefix = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        for i in range(1, ROWS + 1):
            for j in range(1, COLS + 1):
                self.prefix[i][j] = (self.prefix[i - 1][j] + self.prefix[i][j - 1] + matrix[i - 1][j - 1] - self.prefix[i - 1][j - 1])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sAll = self.prefix[row2 + 1][col2 + 1]
        s1 = self.prefix[row1][col1]
        s2 = self.prefix[row2 + 1][col1]
        s3 = self.prefix[row1][col2 + 1]
        return sAll + s1 - s2 - s3


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)