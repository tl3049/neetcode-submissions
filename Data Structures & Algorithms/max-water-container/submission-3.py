class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #brute force
        # n = len(heights)
        # res = 0
        # for l in range(n):
        #     height = heights[l]
        #     for r in range(l+1, n):
        #         area = min(height, heights[r]) * (r - l)
        #         if area > res:
        #             res = area
        # return res
        res = 0
        n = len(heights)
        l, r = 0, n - 1
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res
