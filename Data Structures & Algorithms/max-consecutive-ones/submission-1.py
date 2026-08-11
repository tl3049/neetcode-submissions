class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        res = 0
        while l < len(nums):
            count = 0
            while (l < len(nums)) and (nums[l] == 1) :
                count += 1
                l += 1
            res = max(res, count)
            l += 1
        return res