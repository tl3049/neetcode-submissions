class Solution:
    def trap(self, height: List[int]) -> int:
        #SPACE COMPLEXITY O(N)
        n = len(height)
        maxLeft = [0] * n
        maxRight = [0] * n
        res = 0
        for l in range(1, n):
            maxLeft[l] = max(maxLeft[l-1], height[l-1])
        for r in range(n-2, -1, -1):
            maxRight[r] = max(maxRight[r + 1], height[r + 1])
        for i in range(n):
            area = min(maxLeft[i], maxRight[i]) - height[i]
            if area > 0:
                res += area
        return res 