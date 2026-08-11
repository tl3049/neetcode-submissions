class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        res = 0
        #for loop
        count = 0
        for n in nums:
            if n == 0:
                res = max(res, count)
                count = 0
            else:# n = 1 case
                count += 1
                res = max(res, count)
        return res



        # while l < len(nums):#冗余while
        #     count = 0
        #     while (l < len(nums)) and (nums[l] == 1) :
        #         count += 1
        #         l += 1
        #     res = max(res, count)
        #     l += 1
        # return res