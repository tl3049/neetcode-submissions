class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            dic[num] = i
        for i, num in enumerate(nums):
            rest = target - num
            if (dic.get(rest,-1) != -1) and (dic.get(rest,-1) != i):
                return [i, dic[rest]]
        return 0