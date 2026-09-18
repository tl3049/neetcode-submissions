class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        s = sum(nums)//2
        #dp solution with optimal space complexity
        # dp = [False] * (s + 1)
        # dp[0], dp[nums[0]] = True, True
        # for i in range(1, len(nums)):
        #     for j in range(s, 0, -1):
        #         skip = dp[j]
        #         choose = False
        #         if j >= nums[i]:
        #             choose = dp[j - nums[i]]
        #         dp[j] = skip or choose
        # return dp[-1]

        ##dp solution
        # dp = [[False] * (s + 1) for _ in range(len(nums))]
        # dp[0][nums[0]] = True
        # for i in range(len(nums)):
        #     dp[i][0] = True
        # for i in range(1, len(nums)):
        #     for j in range(1, s+1):
        #         skip = dp[i - 1][j]
        #         choose = False
        #         if j >= nums[i]:
        #             choose = dp[i-1][j - nums[i]]
        #         dp[i][j] = skip or choose
        # return dp[-1][-1]

        cache = [[-1] * (s + 1) for _ in range(len(nums))]
        def dfs(i, val):
            if i == len(nums):
                return True if val == 0 else False
            if cache[i][val] != -1:
                return cache[i][val]

            res = dfs(i + 1, val)#skip
            if val >= nums[i]:
                choose = dfs(i + 1, val - nums[i])
                res = res or choose
            cache[i][val] = res
            return res
        return dfs(0, s)



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