class Solution:
    def climbStairs(self, n: int) -> int:
        #dp with arrays
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


        #memorization
        # memo = {}
        # def dfs(n):
        #     if n <= 2:
        #         return n
        #     if n in memo:
        #         return memo[n]
        #     memo[n] = dfs(n - 1) + dfs(n - 2)
        #     return memo[n]
        # return dfs(n)


























        # #recursion
        # memo = {}
        # def numClimb(k):
        #     if k == 1 or k == 2:
        #         return k
        #     if k in memo:
        #         return memo[k]
        #     else:
        #         res = numClimb(k - 1) + numClimb(k - 2)
        #         memo[k] = res
        #     return es
        # return numClimb(n)





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