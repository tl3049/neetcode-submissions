class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        #Better space compexity
        premax = height[0]
        sufmax = height[-1]
        res = 0
        l, r = 0, n - 1
        while l < r:
            if premax < sufmax:
                h = premax
                if l + 1 < n and h > height[l + 1]:
                    res += h - height[l + 1]
                l += 1
                if l < n:
                    premax = max(premax, height[l])
            else:
                h = sufmax
                if r - 1 >= 0 and h > height[r - 1]:
                    res += h - height[r - 1]
                r -= 1
                if r >= 0:
                    sufmax = max(sufmax, height[r])
        return res
                





        #pre and suf x
        # premax = [0] *n
        # maxVal = height[0]
        # for i in range(n):
        #     if height[i] >= maxVal:
        #         maxVal = height[i]
        #     premax[i] = maxVal
        # sufmax = [0] * n
        # maxVal = height[-1]
        # for i in range(n-1, -1, -1):
        #     if height[i] >= maxVal:
        #         maxVal = height[i]
        #     sufmax[i] = maxVal
        # res = 0
        # for i in range(n):
        #     if i > 0 and i < n - 1:
        #         h = min(premax[i - 1], sufmax[i+1])
        #         if h > height[i]:
        #             res += h - height[i]
        # return res