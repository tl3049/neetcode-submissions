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


        #REDUCE ONE VARIABLE; PREPROCESSING
        # l = 0
        # r = 1 
        # while r < len(nums):
        #     while r < len(nums) and nums[r] == nums[l]:
        #         r += 1
        #     if r == len(nums):
        #         break
        #     nums[l+1] = nums[r]
        #     l += 1
        #     r += 1
        # return l+1


        # #POST PROCESSING
        # l = 0
        # r = 0 
        # while r < len(nums):
        #     nums[l] = nums[r]
        #     while r < len(nums) and nums[r] == nums[l]:
        #         r += 1
        #     l += 1
        # return l


        ##SOLUTION USING FOR
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l 

