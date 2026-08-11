class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        sorted_dict = dict(sorted(dic.items(), key = lambda x: x[1], reverse = True))
        print(sorted_dict)
        opt = []
        for i, key in enumerate(sorted_dict.keys()):
            if i < k:
                opt.append(key)
        return opt