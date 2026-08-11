class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic1 = {}
        dic2 = {}
        for num in nums:
            dic1[num] = dic1.get(num,0) + 1
            dic2[num] = target - num
        indx = -1
        for i, num in enumerate(nums):
            curval = num
            rest = dic2[num]
            if num == rest:
                if dic1.get(rest, 0) == 2:
                    indx = i
                    break
            else: 
                if dic1.get(rest, 0) > 0:
                    indx = i
                    break
        indx2 = -1
        for i, num in enumerate(nums):
            if rest == num:
                indx2 = i
        return [indx, indx2]
