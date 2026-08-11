class Solution:
    def climbStairs(self, n: int) -> int:
        #recursion
        memo = [0] * (n+1)
        def numClimb(k):
            if k == 1 or k == 2:
                return k
            res1 = res2 = 0
            if k - 1 > 0:
                if not memo[k - 1]:
                    res1 = numClimb(k - 1)
                    memo[k - 1] = res1
                else:
                    res1 = memo[k - 1]
            if k - 2 > 0:
                if not memo[k-2]:
                    res2 = numClimb(k - 2)
                    memo[k - 2] = res2
                else:
                    res2 = memo[k - 2]
            return res1 + res2
        return numClimb(n)








        # dp = [0] * (n+1)
        # dp[0] = dp[1] = 1
        # for i in range(2, n+1):
        #     dp[i] = dp[i - 1] + dp[i-2]#i-1 one more step; i-2 two more step
        # return dp[n]



        # prepre, pre = 1,1
        # if n == 0 or n == 1:
        #     val = 1
        # for i in range(2, n+1):
        #     val = pre + prepre
        #     prepre = pre
        #     pre = val
        # return val