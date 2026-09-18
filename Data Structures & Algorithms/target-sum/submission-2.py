class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i, val):
            if i == len(nums):
                return 1 if val == 0 else 0
            if (i, val) in memo:
                return memo[(i, val)]
            plus = dfs(i + 1, val + nums[i])
            minus = dfs(i + 1, val - nums[i])
            res = plus + minus
            memo[(i, val)] = res
            return res
        return dfs(0, target)
