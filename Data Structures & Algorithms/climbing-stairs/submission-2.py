class Solution:
    def climbStairs(self, n: int) -> int:
        # dp = [0] * (n+1)
        # dp[0] = dp[1] = 1
        # for i in range(2, n+1):
        #     dp[i] = dp[i - 1] + dp[i-2]#i-1 one more step; i-2 two more step
        # return dp[n]
        prepre, pre = 1,1
        if n == 0 or n == 1:
            val = 1
        for i in range(2, n+1):
            val = pre + prepre
            prepre = pre
            pre = val
        return val