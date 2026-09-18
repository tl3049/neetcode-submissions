class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #DP solution


        
        
        #DFS with memo
        memo = {}
        def dfs(i, val):
            if i == len(nums):
                return 1 if val == 0 else 0
            if (i, val) in memo:
                return memo[(i, val)]
            memo[(i, val)]  = dfs(i + 1, val + nums[i]) + dfs(i + 1, val - nums[i])
            return memo[(i, val)] 
        return dfs(0, target)
