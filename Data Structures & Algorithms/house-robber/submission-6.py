class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp without array
        pre = 0
        cur = nums[0]
        n = len(nums)
        for i in range(2, n+1):
            tmp = cur
            cur = max(cur, pre + nums[i - 1])
            pre = tmp
        return cur







        # #dp with array
        # n = len(nums)
        # dp = [0] * (n + 1)
        # dp[1] = nums[0]
        # for i in range(2, n+1):
        #     dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        # return dp[-1]








        # memo = {}
        # def dfs(i):
        #     if i < 0:
        #         return 0
        #     if i == 0:
        #         return nums[i]
        #     if i in memo:
        #         return memo[i]
        #     memo[i] = max(dfs(i - 1), dfs(i - 2) + nums[i]) 
        #     return memo[i]
        # return dfs(len(nums) - 1)


























        # n = len(nums)
        # # dp = [0] * (n+1)
        # # dp[1] = nums[0]
        # # for i in range(2, n+1):
        # #     #rob: dp[i-2] + nums[i-1]; not rob: dp[i-1]
        # #     dp[i] = max(dp[i-2] + nums[i-1], dp[i-1])
        # # return dp[n]
        # prepre, pre = 0, nums[0]
        # for i in range(2, n+1):
        #     val = max(prepre + nums[i-1], pre)
        #     prepre = pre
        #     pre = val
        # return pre
