class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        def dfs(i):
            if i >= len(nums):
                res.append(path[:])
                return
            #Choice 1
            path.append(nums[i])
            dfs(i+1)
            #Choice 2
            path.pop()
            dfs(i+1)
        dfs(0)
        return res 