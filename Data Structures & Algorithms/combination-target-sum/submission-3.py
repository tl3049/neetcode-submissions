class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def dfs(start, target):
            if target == 0:
                res.append(path[:])
                return
            elif target < 0:
                return
            else:
                for i in range(start, len(nums)):
                    path.append(nums[i])
                    dfs(i, target - nums[i])
                    path.pop()
        dfs(0, target)
        return res