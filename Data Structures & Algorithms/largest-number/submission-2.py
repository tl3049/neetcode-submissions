from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        def compare(s1, s2):
            if int(s1 + s2) < int(s2 + s1):
                return 1
            else:
                return -1
        nums.sort(key = cmp_to_key(compare))
        return "0" if nums[0] == "0" else "".join(nums)