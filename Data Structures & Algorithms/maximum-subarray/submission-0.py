class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum = nums[0]
        res = cursum
        for i in range(1, len(nums)):
            if cursum <= 0:
                cursum = nums[i]
            else:
                cursum += nums[i]
            res = max(res, cursum)
        return res