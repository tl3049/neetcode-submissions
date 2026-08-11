class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # dp = [0] * (n+1)
        # dp[1] = nums[0]
        # for i in range(2, n+1):
        #     #rob: dp[i-2] + nums[i-1]; not rob: dp[i-1]
        #     dp[i] = max(dp[i-2] + nums[i-1], dp[i-1])
        # return dp[n]
        prepre, pre = 0, nums[0]
        if n == 1:
            val = nums[0]
        for i in range(2, n+1):
            val = max(prepre + nums[i-1], pre)
            prepre = pre
            pre = val
        return val
