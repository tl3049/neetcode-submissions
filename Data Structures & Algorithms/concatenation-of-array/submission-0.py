class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (n*2)
        for i in range(n*2):
            if i < n:
                ans[i] = nums[i]
            else:
                ans[i] = nums[i - n]
        return ans