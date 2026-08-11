class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r)//2
            if target == nums[m]:
                return m 
            #right portion 
            if nums[m] <= nums[r]:
                if target < nums[m]:
                    r = m - 1
                elif target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
            #left portion
            else:
                if target > nums[m]:
                    l = m + 1
                elif target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
        return -1