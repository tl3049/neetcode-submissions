class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # dic = Counter(nums)
        # res = 0
        # for num in nums:
        #     cur = num  
        #     if cur not in dic:
        #         continue
        #     dic.pop(num)
        #     count = 1
        #     while num + 1 in dic:
        #         dic.pop(num + 1)
        #         num = num + 1
        #         count += 1
        #     while cur - 1 in dic:
        #         dic.pop(cur - 1)
        #         cur -= 1
        #         count += 1
        #     res = max(res, count)
        # return res


        #ONE WHILE
        numSet = set(nums)
        res = 0
        for num in numSet:
            if num - 1 not in numSet:#start from minimum
                length = 1  
                while length + num in numSet:
                    length += 1
                res = max(res, length)
        return res

