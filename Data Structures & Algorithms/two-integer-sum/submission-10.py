class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ##One Pass
        # dic = {}
        # for i, num in enumerate(nums):
        #     if target - num in dic:
        #         return [dic[target - num], i]
        #     else:
        #         dic[num] = i

        #Two pass
        dic = {val:idx for idx, val in enumerate(nums)}
        for i, val in enumerate(nums):
            rest = target - val
            if rest in dic and dic[rest] != i:
                return [i, dic[rest]]
