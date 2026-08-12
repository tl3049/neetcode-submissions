class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def dfs(val,start):
            if val == target:
                res.append(path[:])
                return 
            if val > target:
                return
            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(val + nums[i], i)
                path.pop()
            return
        dfs(0, 0)
        return res
