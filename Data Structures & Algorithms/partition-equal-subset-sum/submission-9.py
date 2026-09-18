class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        s = sum(nums)//2
        #dp solution
        dp = [[False] * (s + 1) for _ in range(len(nums))]
        dp[0][0], dp[0][nums[0]] = True, True
        for i in range(1, len(nums)):
            for j in range(1, s+1):
                skip = dp[i - 1][j]
                choose = False
                if j >= nums[i]:
                    choose = dp[i-1][j - nums[i]]
                dp[i][j] = skip or choose
        #print(dp)
        return dp[-1][-1]





        #DFS with cache
        # cache = {}
        # def dfs(i, val):
        #     if i == len(nums):
        #         return True if val == 0 else False
        #     if (i, val) in cache:
        #         return cache[(i, val)] 
        #     res = dfs(i + 1, val)#skip
        #     if val >= nums[i]:
        #         choose = dfs(i + 1, val - nums[i])
        #         res = res or choose
        #     cache[(i, val)] = res
        #     return res
        # return dfs(0, sum(nums)//2)