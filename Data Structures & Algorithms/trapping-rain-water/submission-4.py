class Solution:
    def trap(self, height: List[int]) -> int:
        #SPACE COMPLEXITY O(N)
        # n = len(height)
        # maxLeft = [0] * n
        # maxRight = [0] * n
        # res = 0
        # for l in range(1, n):
        #     maxLeft[l] = max(maxLeft[l-1], height[l-1])
        # for r in range(n-2, -1, -1):
        #     maxRight[r] = max(maxRight[r + 1], height[r + 1])
        # for i in range(n):
        #     area = min(maxLeft[i], maxRight[i]) - height[i]
        #     if area > 0:
        #         res += area
        # return res 

        #OPTIMAL SPACE COMPLEXITY O(1)
        # res = 0
        # n = len(height) 
        # l, r = 0, n - 1
        # maxL, maxR = 0, 0
        # while l < r:
        #     if height[l] <= height[r]: 
        #         maxL = max(maxL, height[l])
        #         i = l + 1
        #         l += 1
        #         if 0 <= i < n:
        #             area = maxL - height[i]
        #             if area > 0:
        #                 res += area
        #     else:
        #         maxR = max(maxR, height[r])
        #         i = r - 1
        #         r -= 1
        #         if 0 <= i < n:
        #             area = maxR - height[i]
        #             if area > 0:
        #                 res += area
        # return res

        res = 0
        n = len(height) 
        l, r = 0, n - 1
        maxL, maxR = 0, 0
        while l < r:
            if height[l] <= height[r]: 
                maxL = max(maxL, height[l])
                area = maxL - height[l+1]
                l += 1
                
            else:
                maxR = max(maxR, height[r])
                area = maxR - height[r-1]
                r -= 1
            if area > 0:
                res += area
        return res

