class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        k = 0
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                continue
            else:
                nums[k+1] = nums[i]
                k += 1
        return k+1
