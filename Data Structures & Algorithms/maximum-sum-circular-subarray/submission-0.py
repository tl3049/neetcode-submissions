class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curmax, totalmax = nums[0], nums[0]
        curmin, totalmin = nums[0], nums[0]
        n = len(nums)
        sumarray = nums[0]
        for i in range(1, n):
            if curmax < 0:
                curmax = nums[i]
            else:
                curmax += nums[i]
            totalmax = max(totalmax, curmax)
            if curmin < 0:
                curmin += nums[i]
            else:
                curmin = nums[i]
            totalmin = min(totalmin, curmin)   
            sumarray += nums[i]
        if totalmax <= 0:#edge case: all numbers are non-positive
            return totalmax
        else:
            return max(totalmax, sumarray - totalmin)