class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # l = 1
        # r = 1 
        # pre = nums[0]
        # while r < len(nums):
        #     while r < len(nums) and nums[r] == pre:
        #         r += 1
        #     if r == len(nums):
        #         break
        #     nums[l], nums[r] = nums[r], nums[l]
        #     pre = nums[l]
        #     l += 1
        #     r += 1
        # return l


        #reduce one variable
        l = 0
        r = 1 
        while r < len(nums):
            while r < len(nums) and nums[r] == nums[l]:
                r += 1
            if r == len(nums):
                break
            nums[l+1] = nums[r]
            l += 1
            r += 1
        return l+1
