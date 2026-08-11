class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #brute force
        n = len(heights)
        res = 0
        for l in range(n):
            height = heights[l]
            for r in range(l+1, n):
                area = min(height, heights[r]) * (r - l)
                if area > res:
                    res = area
        return res