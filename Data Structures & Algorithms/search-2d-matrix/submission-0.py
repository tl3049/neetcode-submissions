class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_row, n_col = len(matrix), len(matrix[0])

        def getIdx(m):
            r = m // n_col
            c = m % n_col
            return [r, c]
        
        left, right = 0, n_row * n_col - 1
        while left <= right:
            mid = (left + right) // 2
            [mid_r, mid_c] = getIdx(mid)
            val = matrix[mid_r][mid_c]
            if val < target:
                left = mid + 1
            elif val > target:
                right = mid - 1
            else:
                return True
        return False