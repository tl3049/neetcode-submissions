class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        path = []
        ##MULTIPLE ELEMENTS SLECTIONS
        def dfs(start):
            res.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                dfs(i + 1)
                path.pop()
        dfs(0)
        return res



        ##SELECTION OR NOT SELCTION
        # def dfs(i):
        #     if i >= len(nums):
        #         res.append(path[:])
        #         return
        #     path.append(nums[i])
        #     dfs(i + 1)

        #     path.pop()
        #     while i + 1 < len(nums) and nums[i] == nums[i + 1]:
        #         i += 1
        #     dfs(i + 1)
        
        # dfs(0)
        # return res