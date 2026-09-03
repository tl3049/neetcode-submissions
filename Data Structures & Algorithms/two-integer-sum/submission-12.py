from collections import deque
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Duplicate elements, e.g., [2,2,4,4],target = 6
        dic = {}
        res = []
        for i, num in enumerate(nums):
            if num in dic:
                dic[num].append(i)
            else:
                dic[num] = deque([i])
        for i, num in enumerate(nums):
            if num in dic and dic[num]:
                dic[num].popleft()
                rest = target - num
                if rest in dic and dic[rest]:
                    res.append([i, dic[rest].popleft()])
        #print(res)
        return res[0]



        
        
        ##One Pass
        # dic = {}
        # for i, num in enumerate(nums):
        #     if target - num in dic:
        #         return [dic[target - num], i]
        #     else:
        #         dic[num] = i

        ##Two pass
        # dic = {val:idx for idx, val in enumerate(nums)}
        # for i, val in enumerate(nums):
        #     rest = target - val
        #     if rest in dic and dic[rest] != i:#two special cases: e.g. 1,#3#,5 target = 6
        #         return [i, dic[rest]] #5,7,#5# target = 10
