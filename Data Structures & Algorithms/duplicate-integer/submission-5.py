from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = Counter(nums)
        for val in dic.values():
            if val > 1:
                return True
        return False