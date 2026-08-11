class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def srob(lsts):
            r1, r2 = 0,0
            for i in range(len(lsts)):
                val = max(lsts[i]+r1, r2)
                r1 = r2
                r2 = val
            return r2
        
        return max(nums[0],srob(nums[1:]),srob(nums[:-1])) 