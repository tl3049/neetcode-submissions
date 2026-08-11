class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in nums:
            if n - 1 not in numSet:
                i = 1
                while n + i in numSet:
                    i += 1
                if i > longest:
                    longest = i
        return longest

