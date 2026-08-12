class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #Two decision version
        res = []
        path = []
        def dfs(i, val):
            if val == target:
                res.append(path[:])
                return 
            if  i >= len(nums) or val > target:
                return 
            path.append(nums[i])
            dfs(i, val + nums[i])
            path.pop()
            dfs(i+1, val)
            return 
        dfs(0, 0)
        return res
                 
            
        
        
        
        
        
        
        
        
        
        
        
        # res = []
        # path = []
        # def dfs(val,start):
        #     if val == target:
        #         res.append(path[:])
        #         return 
        #     if val > target:
        #         return
        #     for i in range(start, len(nums)):
        #         path.append(nums[i])
        #         dfs(val + nums[i], i)
        #         path.pop()
        #     return
        # dfs(0, 0)
        # return res
