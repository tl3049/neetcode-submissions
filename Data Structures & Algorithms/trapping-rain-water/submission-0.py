class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        premax = [0] *n
        maxVal = height[0]
        for i in range(n):
            if height[i] >= maxVal:
                maxVal = height[i]
            premax[i] = maxVal
        sufmax = [0] * n
        maxVal = height[-1]
        for i in range(n-1, -1, -1):
            if height[i] >= maxVal:
                maxVal = height[i]
            sufmax[i] = maxVal
        res = 0
        for i in range(n):
            if i > 0 and i < n - 1:
                h = min(premax[i - 1], sufmax[i+1])
                if h > height[i]:
                    res += h - height[i]
        return res