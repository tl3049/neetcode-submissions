class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # count = [0] * 3
        # for num in nums:
        #     count[num] += 1
        # i = 0
        # for j in range(3):
        #     for _ in range(count[j]):
        #         nums[i] = j
        #         i += 1
        # return nums

        #one pass solution
        l, r = 0, len(nums) - 1
        i = 0
        while i <= r:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            else:
                i += 1
