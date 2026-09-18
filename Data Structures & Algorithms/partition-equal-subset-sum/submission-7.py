class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        s = sum(nums)//2
        cache = {}
        def dfs(i, val):
            if i == len(nums):
                return True if val == 0 else False
            if (i, val) in cache:
                return cache[(i, val)] 
            res = dfs(i + 1, val)#skip
            if val >= nums[i]:
                choose = dfs(i + 1, val - nums[i])
                res = res or choose
            cache[(i, val)] = res
            return res
        return dfs(0, sum(nums)//2)