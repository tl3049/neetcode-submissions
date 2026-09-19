from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #DP solution
        dp = [defaultdict(int) for _ in range(len(nums) + 1)]
        dp[0][0] = 1
        for i in range(len(nums)):
            for key, value in dp[i].items():
                dp[i+1][key - nums[i]] += value
                dp[i+1][key + nums[i]] += value
        return dp[-1][target]

        
        
        #DFS with memo
        # memo = {}
        # def dfs(i, val):
        #     if i == len(nums):
        #         return 1 if val == 0 else 0
        #     if (i, val) in memo:
        #         return memo[(i, val)]
        #     memo[(i, val)]  = dfs(i + 1, val + nums[i]) + dfs(i + 1, val - nums[i])
        #     return memo[(i, val)] 
        # return dfs(0, target)
