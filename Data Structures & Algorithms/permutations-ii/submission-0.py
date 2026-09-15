class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        path = []
        used = [False] * len(nums)
        def dfs():
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if (i > 0 and nums[i] == nums[i - 1]) and (not used[i - 1]):
                    continue
                if not used[i]:
                    path.append(nums[i])
                    used[i] = True
                    dfs()
                    used[i] = False
                    path.pop()
        dfs()
        return res