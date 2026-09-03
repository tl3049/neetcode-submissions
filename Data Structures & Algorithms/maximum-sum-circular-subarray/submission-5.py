class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax, totalMax = nums[0], nums[0]
        curMin, totalMin = nums[0], nums[0]
        n = len(nums)
        total = nums[0]
        for i in range(1, n):
            # if curMax < 0:
            #     curMax = nums[i]
            # else:
            #     curMax += nums[i]
            curMax = max(curMax + nums[i], nums[i])
            totalMax = max(totalMax, curMax)
            # if curMin < 0:
            #     curMin += nums[i]
            # else:
            #     curMin = nums[i]
            curMin = min(curMin + nums[i], nums[i])
            totalMin = min(totalMin, curMin)   
            total += nums[i]
        return totalMax if totalMax <= 0 else max(totalMax, total - totalMin)
        # if totalMax <= 0:#edge case: all numbers are non-positive
        #     return totalMax
        # else:
        #     return max(totalMax, total - totalMin)