class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        output = []
        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, n - 1
            target = -nums[i]
            while l < r:
                val = nums[l] + nums[r]
                if val < target:
                    l += 1
                elif val > target:
                    r -= 1
                else:
                    output.append([nums[i], nums[l], nums[r]])
                    while l < n-1 and nums[l] == nums[l+1]:
                        l += 1
                    while nums[r] == nums[r-1] and r > 0:
                        r -= 1
                    l += 1
                    r -= 1
        return output


